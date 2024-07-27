import base64
import configparser
import gc
import json
import logging
import os
import queue
import shutil
import socket
import threading
import time
from abc import ABC, abstractmethod

import librosa
import numpy as np

from src._enum import BLUE, ENDC, GREEN
from src.utils.audio_recognizer import AudioRecognizer
from src.utils.audio_recorder import AudioRecorder
from src.utils.audio_utils import read_byte_from_wav, write_frames_to_file
from src.utils.auga import normalize_rms
from src.utils.error_utils import RecordingError, TranscribingError
from src.utils.influx_client import InfluxDBClientWrapper
from src.utils.input_utils import get_function_base, get_id
from src.utils.logger_utils import get_logger
from src.utils.mqtt_client import MQTTClientWrapper
from src.utils.os_utils import clear_directory
from src.utils.redis_client import RedisClientWrapper
from src.utils.request_utils import request_speech_transcription, request_speech_separation
from src.utils.thread_utils import RaisingThread

try:
    from src.utils.transcriber import Transcriber
except ImportError:
    Transcriber = None

try:
    import torch
except ImportError:
    torch = None

try:
    from modelscope.pipelines import pipeline
    from modelscope.utils.constant import Tasks
except ImportError:
    pipeline, Tasks = None, None


class AudioBase(ABC):
    logger = get_logger(f'audio-base')

    def __init__(self, root_dir: str = None, config_path: str = None, mode: str = 'full', local: bool = False,
                 vad: bool = True, nr: bool = True, tr: bool = True, sp: bool = False, store: bool = True):
        """Initialize the Audio Base.

        :param root_dir: root directory of the project
        :param config_path: path to the configuration file
        :param mode: operating mode
        :param local: whether to run the audio base locally
        :param vad: whether to use the VAD
        :param nr: whether to use the denoiser to enhance speech
        :param tr: whether to transcribe speech to text
        :param sp: whether to do speech separation for overlapped segment
        :param store: whether to store audio files
        """
        # Arguments passed from the subclass
        self.root_dir = root_dir if root_dir else os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        self.config_path = os.path.join(self.root_dir, config_path if config_path else 'conf/audio_base.ini')
        self.mode = mode
        self.local = local
        self.vad = vad
        self.nr = nr
        self.tr = tr
        self.sp = sp
        self.store = store

        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        self.audio_realtime_dir = os.path.join(self.root_dir, 'audio', 'real-time')
        self.audio_temp_dir = os.path.join(self.root_dir, 'audio', 'temp')
        self.audio_db_dir = os.path.join(self.root_dir, 'audio_db')

        # Runtime variables
        self.bucket_name = None
        self.last_speaker = None
        self.audio_dir = None
        self.audio_queue = None
        self.transcription_queue = None
        self.speaker_frames_dict = None
        self.threads = []
        self.stop_event = threading.Event()

        # Attributes to be initialized in the subclass
        self.register_duration = None  # segment length of speaker registration
        self.recognize_duration = None  # segment length of speaker recognition
        self.rms_threshold = None  # volume energy level RMS threshold
        self.rms_peak_threshold = None  # volume energy level RMS peak threshold
        self.threshold = None  # similarity threshold for speaker recognition
        self.keep_threshold = None  # similarity threshold for keep speaker when doing half-scaled recognition
        self.audio_server_host = None  # audio server host IP

        self.config = None  # config object
        self.influx_client = None  # InfluxDB client object
        self.redis_client = None  # Redis client object
        self.mqtt_client = None  # MQTT client object
        self.audio_recognizer = None  # audio recognizer object
        self.audio_recorder = None  # audio recorder object
        self.speech_transcriber = None  # speech transcriber object
        self.speech_separator = None  # speech separator object

        self.id = None  # audio base id
        self.audio_db = None  # audio database directory

        self._load_config()
        self._config_from_user()
        self._config_objects()

    @property
    @abstractmethod
    def base_type(self):
        """Return the type of the audio base."""
        pass

    def _load_config(self):
        """Configure the audio base based on the arguments passed from the subclass."""
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.register_duration = int(self.config[self.base_type]['register_duration'])
        self.rms_threshold = int(self.config[self.base_type]['rms_threshold'])
        self.rms_peak_threshold = int(self.config[self.base_type]['rms_peak_threshold'])
        self.threshold = float(self.config[self.base_type]['recognize_sp_threshold']) if self.sp else float(
            self.config[self.base_type]['recognize_threshold'])
        self.keep_threshold = float(self.config[self.base_type]['keep_sp_threshold']) if self.sp else float(
            self.config[self.base_type]['keep_threshold'])
        self.recognize_duration = int(self.config[self.base_type]['recognize_sp_duration']) if self.sp else int(
            self.config[self.base_type]['recognize_duration'])
        self.audio_server_host = socket.gethostbyname(self.config['Server']['audio_server_host'])

    def _config_from_user(self):
        """Configure the audio base based on the user input."""
        self.id = get_id()
        self.audio_db = os.path.join(self.audio_db_dir, f'{self.base_type}_{self.id}')
        os.makedirs(self.audio_db, exist_ok=True)

    def _config_objects(self):
        """Configure the audio base based on the configuration file."""
        self.influx_client = InfluxDBClientWrapper(self.config_path)
        self.redis_client = RedisClientWrapper(self.config_path)
        self.mqtt_client = MQTTClientWrapper(self.config_path)
        self.warm_up_resampler()

        if self.local:
            self.audio_recorder = AudioRecorder(config_path=self.config_path, vad_enable=self.vad, nr_enable=self.nr,
                                                nr_local=True, vad_local=True)
            self.audio_recognizer = AudioRecognizer(config_path=self.config_path, audio_db=self.audio_db, local=True,
                                                    model_path=self.config['Local']['sr_model'])
            if self.tr:
                if Transcriber is None:
                    raise ImportError("Transcriber module is not available, please install the required dependencies.")
                self.speech_transcriber = Transcriber(self.config['Local']['tr_model'],
                                                      self.config['Local']['language'])

            if self.sp:
                if pipeline is None or Tasks is None:
                    raise ImportError("Modelscope module is not available, please install the required dependencies.")
                logging.getLogger('modelscope').setLevel(logging.WARNING)
                device = 'gpu' if torch.cuda.is_available() else 'cpu'
                try:
                    self.speech_separator = pipeline(Tasks.speech_separation, device=device,
                                                     model=self.config['Local']['sp_model'])
                except ValueError:
                    self.separator = pipeline(Tasks.speech_separation, device=device,
                                              model=self.config['Local']['sp_model_local'])
        else:
            self.audio_recorder = AudioRecorder(config_path=self.config_path, vad_enable=self.vad, nr_enable=self.nr)
            self.audio_recognizer = AudioRecognizer(config_path=self.config_path, audio_db=self.audio_db)

    def run(self):
        """Interface for running the Audio Base."""
        func_map = {1: self._register_profile, 2: self._recognize_voice, 3: self._reset, 4: self._switch_mode}
        while True:
            try:
                print(f"\033]0;Audio Base {self.base_type} {self.id} \007")
                select_fun = get_function_base()
                if select_fun == 0:
                    print("------------------------------------------------")
                    clear_directory(self.audio_temp_dir)
                    self.logger.info("Exiting the program...")
                    break
                func_map.get(select_fun, lambda: self.logger.warning("Invalid option"))()
            except (Exception, KeyboardInterrupt) as e:
                self._clean_up()
                self.logger.warning(
                    f"During running the audio base, catch: {'KeyboardInterrupt' if isinstance(e, KeyboardInterrupt) else e}, Come back to the main menu.",
                    exc_info=True)

    @abstractmethod
    def _register_profile(self):
        """Register participant's voice to audio database."""
        pass

    @abstractmethod
    def _recognize_voice(self):
        """Start the real-time voice recognition, including audio recording, speaker recognition,
        speech transcription, and listening on stop signal."""
        pass

    @abstractmethod
    def _reset(self):
        """Set the new port for the audio base and reinitialize audio base."""
        pass

    @abstractmethod
    def _switch_mode(self):
        """Switch the mode of the audio base."""
        pass

    def _create_thread(self, target, *args):
        """Create a new thread and add it to the thread list.

        :param target: the target function to run in the thread
        """
        t = RaisingThread(target=target, args=args)
        self.threads.append(t)

    def _start_threads(self):
        """Start all threads."""
        self.stop_event.clear()
        for t in self.threads:
            t.start()

    def _join_threads(self):
        """Wait for all threads to finish."""
        for t in self.threads:
            t.join()

    def _stop_threads(self):
        """Stop all threads and free memory."""
        self.stop_event.set()
        for t in self.threads:
            if threading.current_thread() != t:
                try:
                    t.join(timeout=5)
                except Exception as e:
                    self.logger.warning(f"During the thread stopping, catch: {e}")
        self.threads.clear()

    def _clean_up(self):
        """Free memory by resetting the runtime variables."""
        self.bucket_name = None
        self.last_speaker = None
        self.audio_dir = None
        self.audio_queue = None
        self.transcription_queue = None
        self.speaker_frames_dict = None
        gc.collect()

    def _listen_for_start_signal(self):
        """Listen on the redis bucket control channel for the START signal."""
        p = self.redis_client.subscribe(f'{self.bucket_name}/control')  # Note: pubsub is not thread-safe
        self.logger.info("Wait for START signal...")
        while True:
            message = p.get_message()
            if message and message['data'] == b'START':
                self.logger.info("Received START signal, start recognizing...")
                break

    def _listen_for_stop_signal(self):
        """Listen on the redis bucket control channel for the STOP signal."""
        p = self.redis_client.subscribe(f'{self.bucket_name}/control')
        self.logger.info("Listening for STOP signal...")
        while not self.stop_event.is_set():
            message = p.get_message()
            if message and message['data'] == b'STOP':
                self.logger.info("Received STOP signal, stop recognizing...")
                self._stop_threads()

    def _load_and_queue_recorded_files(self):
        """Load pre-recorded audio files and queue them for recognition when in recognize mode."""
        while not self.stop_event.is_set():
            try:
                print(f"{GREEN}[Pre-recorded Audio]{ENDC}Loading pre-recorded audio files...")
                audio_files = [os.path.join(self.audio_dir, 'records', f) for f in
                               os.listdir(os.path.join(self.audio_dir, 'records'))
                               if f.endswith('.wav')]
                audio_files_sorted = sorted(audio_files, key=lambda x: os.path.getmtime(x))

                for file_path in audio_files_sorted:
                    frames = read_byte_from_wav(file_path)
                    temp_file_path = os.path.join(self.audio_dir, 'temp', os.path.basename(file_path))
                    self.audio_queue.put((temp_file_path, frames))
                print(f"{GREEN}[Pre-recorded Audio]{ENDC}Pre-recorded audio files loaded and queued.")
                return
            except Exception as e:
                raise RecordingError(
                    f'RecordingError occurred when loading pre-recorded audio files and queue: {e}') from e

    def _continuous_transcribing(self):
        """Continuously transcribe audio from the transcription queue."""
        while not self.stop_event.is_set():
            try:
                frames, speaker, chunk_start_time, chunk_end_time = self.transcription_queue.get(timeout=2)
                text = self._transcribe(frames)
                self._upload_transcription_data(speaker, text, chunk_start_time, chunk_end_time)
            except queue.Empty:
                continue
            except Exception as e:
                raise TranscribingError(f'TranscribingError occurred when transcribing: {e}') from e

    def _update_chunk_list(self, left_speaker, right_speaker, last_speaker, current_speaker, chunk_frames, frames,
                           record_start_time):
        """Update the chunk list based on the half-scaled recognition results at the speaker turn border.

        :param left_speaker: recognized speaker of the left half-segment
        :param right_speaker: recognized speaker of the right half-segment
        :param last_speaker: recognized speaker of the last segment
        :param current_speaker: recognized speaker of the current segment
        :param chunk_frames: audio frames of the current chunk belonging to the last speaker
        :param frames: audio frames of the current segment
        :param record_start_time: record start time of the current segment
        """
        num_frames = int(len(frames) / 2)

        if left_speaker == right_speaker and left_speaker == last_speaker:  # Case AAAB: Extend the left chunk
            chunk_frames = chunk_frames + frames[:num_frames]
            frames = frames[num_frames:]
            record_start_time = str(float(record_start_time) + self.recognize_duration / 2)
            chunk_end_time = record_start_time
        elif left_speaker == right_speaker and right_speaker == current_speaker:  # Case ABBB: Extend the right chunk
            frames = chunk_frames[-num_frames:] + frames
            chunk_frames = chunk_frames[:-num_frames]
            record_start_time = str(float(record_start_time) - self.recognize_duration / 2)
            chunk_end_time = record_start_time
        else:  # Other cases, AABB, A_BB, AA_B, A__B (excluding ABAB, AB_B, A_AB)
            chunk_end_time = record_start_time
            if left_speaker != last_speaker:
                chunk_frames = chunk_frames[:-num_frames]
                chunk_end_time = str(float(record_start_time) - self.recognize_duration / 2)
            if right_speaker != current_speaker:
                frames = frames[num_frames:]
                record_start_time = str(float(record_start_time) + self.recognize_duration / 2)

        return chunk_frames, frames, record_start_time, chunk_end_time

    def _add_to_transcription_queue(self, frames, speaker, chunk_start_time, chunk_end_time):
        """Add transcription data to the transcription queue.

        :param frames: audio frames to be transcribed
        :param speaker: recognized speaker of the audio frames
        :param chunk_start_time: start time of the audio frames
        :param chunk_end_time: end time of the audio frames
        """
        if self.tr:
            self.transcription_queue.put((frames, speaker, chunk_start_time, chunk_end_time))

    def _transcribe(self, frames):
        """Transcribe audio frames to text.

        :param frames: audio frames to be transcribed
        :return: transcribed text
        """
        if self.local:
            fr = 8000 if self.sp else 16000
            audio_file_path = os.path.join(self.audio_temp_dir, f'transcribe_audio_{self.base_type}_{self.id}.wav')
            write_frames_to_file(output_path=audio_file_path, frames=frames, channels=1, sampwidth=2, framerate=fr)
            if fr == 16000:
                self.audio_recorder.apply_nr(audio_file_path)
            normalize_rms(infile=audio_file_path, rms_level=-20)
            text = self.speech_transcriber.transcribe(audio_file_path)
        else:
            text = request_speech_transcription(frames, f'{self.base_type.lower()}_{self.id}', self.sp,
                                                self.audio_server_host)
        return text

    def _separate_speech(self, segment_audio_path):
        """Separate speech from the overlapped segment audio.

        :param segment_audio_path:
        :return: separated speech signals
        """
        if self.local:
            separated_result = self.speech_separator(segment_audio_path)
            result = separated_result['output_pcm_list']
        else:
            separated_result = request_speech_separation(segment_audio_path, f'{self.base_type.lower()}_{self.id}',
                                                         self.audio_server_host)
            result = [base64.b64decode(encoded_bytes_stream) for encoded_bytes_stream in separated_result]
        return result

    def _upload_transcription_data(self, speaker, text, chunk_start_time, chunk_end_time):
        """Upload transcription data to InfluxDB.

        :param speaker: recognized speaker name of the transcribed chunk
        :param text: transcribed text of the chunk
        :param chunk_start_time: start time of the chunk
        :param chunk_end_time:  end time of the chunk
        """
        transcription_data = {
            "measurement": "speaker transcription",
            "fields": {
                "chunk_start_time": float(chunk_start_time),
                "chunk_end_time": float(chunk_end_time),
                "text": text,
                "speaker": speaker,
            },
        }
        print(f"{GREEN}[Speaker Transcription]{ENDC}{transcription_data['fields']['chunk_start_time']}: "
              f"{GREEN}{speaker} : {text}{ENDC}")
        self.influx_client.write(self.bucket_name, record=transcription_data)

    def _log_and_publish_results(self, record_start_time, recognize_start_time, speakers, similarities, durations):
        """Log and publish base speaker recognition results in Json string to Redis on bucket channel.

        :param record_start_time: record start time of the segment
        :param recognize_start_time: start time of the recognition process
        :param speakers: recognized speakers
        :param similarities: similarity values
        :param durations: audio durations
        """
        base_recognition_result = {
            'base_id': f'{self.base_type.lower()}_{self.id}',
            'record_start_time': record_start_time,
            'speakers': json.dumps(speakers),
            'similarities': json.dumps(similarities),
            'durations': json.dumps(durations)
        }
        print(f"{BLUE}[Speaker Recognition]{ENDC}{base_recognition_result['record_start_time']}: "
              f"{BLUE}{base_recognition_result['speakers']}{ENDC}, similarity: {base_recognition_result['similarities']},"
              f"processed time: {time.time() - recognize_start_time} seconds")
        result_str = json.dumps(base_recognition_result)
        self.mqtt_client.publish(f'{self.bucket_name}/audio', result_str)

    def _prepare_directories(self):
        """Prepare and manage directories based on the operation mode."""
        sub_dirs = ['segments', 'chunks', 'separations', 'temp', 'records']
        for subdir in sub_dirs:
            directory_path = os.path.join(self.audio_dir, subdir)
            os.makedirs(directory_path, exist_ok=True)

        if self.mode == 'recognize':
            for subdir in ['segments', 'chunks', 'separations']:
                clear_directory(os.path.join(self.audio_dir, subdir))

        if self.mode == 'record':
            clear_directory(os.path.join(self.audio_dir, 'records'))

        clear_directory(os.path.join(self.audio_dir, 'temp'))

    def _store_audio(self, source_path, dest_path):
        """Store or remove audio files based on the store flag.

        :param source_path: original audio file path
        :param dest_path: destination audio file path
        """
        if self.store:
            shutil.move(source_path, dest_path)
        else:
            os.remove(source_path)

    def _finalize_sp_results(self, speakers, similarities, durations, signals):
        """Post-process the recognition results of separated signals to handle edge cases.

        :param speakers: list of recognized speakers
        :param similarities: list of similarity values
        :param durations: list of audio durations
        :param signals: list of separated signals
        :return: post-processed speakers, similarities, durations, signals
        """
        # If there's only one speaker, keep it as is
        if len(speakers) == 1:
            return speakers, similarities, durations, signals

        # If both speakers are the same, keep the one with the highest similarity
        if speakers[0] == speakers[1]:
            max_similarity_index = 0 if similarities[0] > similarities[1] else 1
            return [speakers[max_similarity_index]], [similarities[max_similarity_index]], [
                durations[max_similarity_index]], [signals[max_similarity_index]]

        # If both are real speakers, keep them as is
        if all(speaker not in ['silent', 'unknown'] for speaker in speakers):
            return speakers, similarities, durations, signals

        # If there's at least one real speaker, keep only the real ones
        real_speakers, real_similarities, real_durations, real_texts = self.filter_real_speakers(speakers, similarities,
                                                                                                 durations, signals)
        if real_speakers:
            return real_speakers, real_similarities, real_durations, real_texts

        # Special cases for 'silent' and 'unknown'
        if 'unknown' in speakers and 'silent' in speakers:
            return (['unknown'], [similarities[speakers.index('unknown')]], [durations[speakers.index('unknown')]],
                    [signals[speakers.index('unknown')]])
        if speakers.count('silent') == 2:
            return ['silent'], [similarities[0]], [durations[0]], [signals[0]]
        if speakers.count('unknown') == 2:
            max_index = durations.index(max(durations))
            return ['unknown'], [similarities[max_index]], [durations[max_index]], [signals[max_index]]

        return [], [], [], []

    @staticmethod
    def filter_real_speakers(speakers, similarities, durations, texts):
        """Filter out 'silent' and 'unknown' from speakers and their associated similarities and durations.

        :param speakers: list of speakers
        :param similarities: list of similarities
        :param durations: list of durations
        :param texts: list of texts
        :return: list of real_speakers, real_similarities, real_durations, real_texts
        """
        real_speakers = []
        real_similarities = []
        real_durations = []
        real_texts = []
        for i, speaker in enumerate(speakers):
            if speaker not in ['silent', 'unknown']:
                real_speakers.append(speaker)
                real_similarities.append(similarities[i])
                real_durations.append(durations[i])
                real_texts.append(texts[i])

        return real_speakers, real_similarities, real_durations, real_texts

    @staticmethod
    def warm_up_resampler(sample_rate_original=44100, sample_rate_target=16000):
        """Warm up the resampler by generating a short segment of silence and performing the resampling operation, to
        avoid delay in the first resampling operation.

        :param sample_rate_original: original sample rate, default to 44100
        :param sample_rate_target: target sample rate, default to 16000
        """
        dummy_audio = np.zeros(sample_rate_original)
        _ = librosa.resample(dummy_audio, orig_sr=sample_rate_original, target_sr=sample_rate_target)
        print("Resampler has been warmed up.")

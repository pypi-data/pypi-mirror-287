import configparser
import json
import logging
import os
import shutil
from datetime import datetime, timedelta

import numpy as np
import soundfile as sf
from tqdm import tqdm

from src.utils.audio_recognizer import AudioRecognizer
from src.utils.audio_recorder import AudioRecorder
from src.utils.audio_utils import format_wav, get_audio_properties, segment_wav, crop_and_concatenate_wav, resample
from src.utils.auga import normalize_rms
from src.utils.file_utils import convert_transcription_json_to_txt
from src.utils.analyze_utils import plot_speaking_interaction_network, plot_speaker_diarization_interactive
from src.utils.logger_utils import get_logger
from src.utils.transcriber import Transcriber


class AudioPostAnalyzer:
    logger = get_logger('audio-post-analyzer')

    def __init__(self, root_dir: str = None, config_path: str = None, filename: str = None, vad: bool = True,
                 nr: bool = True, sp: bool = True, tr: bool = True):
        np.random.seed(1)
        self.root_dir = root_dir if root_dir else os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        self.config_path = os.path.join(self.root_dir, config_path if config_path else 'conf/audio_base.ini')
        self.filename = filename
        self.vad = vad
        self.nr = nr
        self.sp = sp
        self.tr = tr

        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        self.speakers_corpus_dir = os.path.join(self.root_dir, 'audio_db', 'post-time')
        self.audio_origin_dir = os.path.join(self.root_dir, 'audio', 'post-time', 'origin')
        self.audio_formatted_dir = os.path.join(self.root_dir, 'audio', 'post-time', 'formatted')
        self.audio_segments_dir = os.path.join(self.root_dir, 'audio', 'post-time', 'segments')
        self.audio_chunks_dir = os.path.join(self.root_dir, 'audio', 'post-time', 'chunks')
        self.audio_temp_dir = os.path.join(self.root_dir, 'audio', 'temp')
        self.audio_db_dir = os.path.join(self.root_dir, 'audio_db')
        self.logs_dir = os.path.join(self.root_dir, 'logs')
        self.visualizations_dir = os.path.join(self.root_dir, 'visualizations')

        filenames_in_dir = [f for f in os.listdir(self.audio_origin_dir) if not f.startswith('.')]
        self.filenames_to_process = [filename] if filename else filenames_in_dir
        if not self.filenames_to_process:
            raise ValueError("You must specify an audio file to process or place it under the audio/post-time/origin "
                             "folder.")

        config = configparser.ConfigParser()
        config.read(self.config_path)
        self.frame_rate = int(config['PostAnalyzer']['frame_rate'])
        self.channels = int(config['PostAnalyzer']['channels'])
        self.sample_width = int(config['PostAnalyzer']['sample_width'])
        self.segment_duration = int(config['PostAnalyzer']['segment_duration'])
        self.threshold = float(config['PostAnalyzer']['threshold'])
        self.keep_threshold = float(config['PostAnalyzer']['keep_threshold'])
        self.sr_model = config['PostAnalyzer']['sr_model']
        self.language = config['PostAnalyzer']['language']

        if self.tr:
            self.transcriber = Transcriber(config['PostAnalyzer']['tr_model'], language=self.language, use_cuda=False)
        if self.sp:
            from modelscope.pipelines import pipeline
            from modelscope.utils.constant import Tasks
            logging.getLogger('modelscope').setLevel(logging.WARNING)
            try:
                self.separator = pipeline(Tasks.speech_separation, model=config['PostAnalyzer']['sp_model'])
            except ValueError:
                self.separator = pipeline(Tasks.speech_separation, model=config['PostAnalyzer']['sp_model_local'])

        self.recorder = AudioRecorder(config_path=self.config_path, vad_enable=self.vad, nr_enable=self.nr,
                                      use_onnx=False,
                                      use_cuda=True, vad_local=True, nr_local=True)
        self.recognizer = AudioRecognizer(
            config_path=self.config_path,
            audio_db=os.path.join(self.audio_db_dir, os.path.splitext(self.filenames_to_process[0])[0]),
            model_path=self.sr_model, use_onnx=False, use_cuda=True, local=True)

    def run(self):
        """Process all specified files under the audio/post-time/origin folder."""
        for audio_file_name in tqdm(self.filenames_to_process, desc='Processing audio files', unit='session'):
            if audio_file_name.endswith('.DS_Store'):
                continue
            self._process_single_audio_file(audio_file_name)
            self.logger.info(f"Processing file: {audio_file_name}")

    def _process_single_audio_file(self, filename):
        session_name = os.path.splitext(filename)[0]  # Get the session name from the filename without extension
        speakers_corpus_dir = os.path.join(self.speakers_corpus_dir, session_name)

        if not os.path.exists(speakers_corpus_dir):
            os.makedirs(speakers_corpus_dir)
            raise ValueError(
                f"{speakers_corpus_dir} not exist, please add your raw speaker corpus for {filename}")

        if not os.listdir(speakers_corpus_dir):
            raise ValueError(
                f"{speakers_corpus_dir} is empty, please add your raw speaker corpus for {filename}")

        logs_dir = os.path.join(self.logs_dir, f'session_{session_name}')
        os.makedirs(logs_dir, exist_ok=True)

        # Reset audio recognizer's audio database
        speakers_db = os.path.join(self.audio_db_dir, session_name)
        self.recognizer.reset_db(speakers_db)

        #  Register speakers' raw audio files, set enhance to True to apply NR and VAD for the first time
        self._register_audio_file_speakers(speakers_corpus_dir, enhance=False)

        # Format the origin audio file, segment it, and process the segments
        formatted_audio_file_path = self._format_origin_audio_file(filename)
        self._segment_audio_file(session_name, formatted_audio_file_path)
        if self.sp:
            self._process_segments_sp(session_name)
        else:
            self._process_segments(session_name)

    def _register_audio_file_speakers(self, speakers_corpus_dir, enhance=False):
        for speaker_raw_audio in os.listdir(speakers_corpus_dir):
            if speaker_raw_audio.endswith('.DS_Store'):
                continue
            speaker_raw_audio_path = os.path.join(speakers_corpus_dir, speaker_raw_audio)
            self.logger.info(f"Speaker raw audio path: {speaker_raw_audio_path}")
            if enhance:
                self.recorder.apply_nr(input_path=speaker_raw_audio_path)
                self.recorder.apply_vad(input_path=speaker_raw_audio_path, sampling_rate=16000, inplace=True)
            self.recognizer.register(speaker_raw_audio_path, speaker_raw_audio.split('.')[0])

    def _format_origin_audio_file(self, filename):
        input_file_path = os.path.join(self.audio_origin_dir, filename)
        output_file_path = os.path.join(self.audio_formatted_dir, f'{os.path.splitext(filename)[0]}_formatted.wav')
        format_wav(input_file_path, output_file_path)
        properties = get_audio_properties(output_file_path)
        for key, value in properties.items():
            print(f'{key}: {value}')

        return output_file_path

    def _segment_audio_file(self, session_name, formatted_audio_file_path):
        output_dir = os.path.join(self.audio_segments_dir, session_name)
        segment_wav(formatted_audio_file_path, output_dir, window_length_ms=int(self.segment_duration * 1000))

    def _process_segments(self, session_name):
        segments_dir = os.path.join(self.audio_segments_dir, session_name)
        speaker_recognition_log_path = os.path.join(self.logs_dir, f'session_{session_name}',
                                                    f'session_{session_name}_speaker_recognition.json')
        speaker_transcription_log_path = os.path.join(self.logs_dir, f'session_{session_name}',
                                                      f'session_{session_name}_speaker_transcription.json')
        visualization_dir = os.path.join(self.visualizations_dir, f'session_{session_name}')
        os.makedirs(visualization_dir, exist_ok=True)

        segments_path_list = sorted(
            [os.path.join(segments_dir, file) for file in os.listdir(segments_dir)],
            key=lambda x: int(os.path.basename(x).split('_')[-1][:-4])
        )

        start_time = datetime.now()  # starting datetime object of the conversation
        time = timedelta(seconds=0)
        segment_no = 0
        speaker_recognition_log_entries = []

        with tqdm(total=len(segments_path_list), desc=f"Processing segments for {session_name}",
                  unit="segment", position=0, leave=True) as pbar:
            for segment_path in segments_path_list:
                assert isinstance(segment_path, str), "segment_path must be a string"
                if segment_path.endswith('.DS_Store'):
                    continue

                processed_segment_path = self.recorder.post_processing(segment_path, sampling_rate=16000, inplace=True)

                # Create speaker recognition log entry and update the speaker_recognition_log_entries list
                speaker = 'silent' if processed_segment_path is None else 'unknown'
                similarity = 0
                duration = self.segment_duration

                if processed_segment_path:
                    duration = self.calculate_audio_duration(segment_path)
                    normalize_rms(segment_path, rms_level=-20)
                    name, similarity = self.recognizer.recognize(segment_path, update_threshold=0.5)
                    if similarity > self.threshold:
                        speaker = name

                time += timedelta(seconds=self.segment_duration)
                segment_start_time = int((start_time + time).timestamp())
                recognition_entry = {
                    "segment_no": segment_no,
                    "segment_start_time": segment_start_time,
                    "speakers": json.dumps([speaker]),
                    "similarities": json.dumps([np.round(np.float64(similarity), 4)]),
                    "durations": json.dumps([duration]),
                }
                speaker_recognition_log_entries.append(recognition_entry)
                segment_no += 1
                pbar.update()

        # Write all speaker_recognition_log_entries to the JSON file at once
        with open(speaker_recognition_log_path, 'w') as f:
            json.dump(speaker_recognition_log_entries, f, indent=5)

        # Visualize the speaker recognition results
        plot_speaking_interaction_network(speaker_recognition_log_path, visualization_dir)
        plot_speaker_diarization_interactive(speaker_recognition_log_path, visualization_dir)

        # Process half-scaled recognition at speaker change borders
        formatted_audio_file_path = os.path.join(self.audio_formatted_dir, f'{session_name}_formatted.wav')
        chunk_list = self._aggregate_segments_by_speaker(speaker_recognition_log_path)
        borders = self.identify_speaker_change_borders(chunk_list)  # A list of tuple, (border_time, [candidates])
        added_chunks_no = 0
        for index, (border_time, candidates) in enumerate(borders):
            adjusted_index = index + added_chunks_no
            left_temp_path = os.path.join(self.audio_temp_dir, 'left_temp_post_analyzer.wav')
            right_temp_path = os.path.join(self.audio_temp_dir, 'right_temp_post_analyzer.wav')
            left_start_time = max(0, 1000 * (border_time - self.segment_duration / 2))  # Segment before the border
            right_end_time = 1000 * (border_time + self.segment_duration / 2)  # Segment after the border
            crop_and_concatenate_wav(formatted_audio_file_path, [(left_start_time, 1000 * border_time)], left_temp_path)
            crop_and_concatenate_wav(formatted_audio_file_path, [(1000 * border_time, right_end_time)], right_temp_path)

            if self.recorder.apply_vad(left_temp_path, sampling_rate=16000, inplace=False):
                left_speaker, _ = self.recognizer.recognize_among_candidates(left_temp_path, candidates,
                                                                             candidates[0], self.keep_threshold)
            else:
                left_speaker = 'silent'

            if self.recorder.apply_vad(right_temp_path, sampling_rate=16000, inplace=False):
                right_speaker, _ = self.recognizer.recognize_among_candidates(right_temp_path, candidates,
                                                                              candidates[1], self.keep_threshold)
            else:
                right_speaker = 'silent'

            result = self.update_chunk_list(chunk_list, adjusted_index, left_speaker, right_speaker,
                                            self.segment_duration / 2)
            if result:
                added_chunks_no += result

        # Aggregate the chunks and transcribe them
        chunk_list = self.aggregate_chunks(chunk_list)
        speaker_transcription_log_entries = self._transcribe_by_chunks(formatted_audio_file_path, chunk_list,
                                                                       session_name)

        with open(speaker_transcription_log_path, 'w') as f:
            json.dump(speaker_transcription_log_entries, f, indent=5)

        convert_transcription_json_to_txt(speaker_transcription_log_path)

    def _process_segments_sp(self, session_name):
        speaker_recognition_log_path = os.path.join(self.logs_dir, f'{session_name}',
                                                    f'session_{session_name}_speaker_recognition.json')
        speaker_transcription_log_path = os.path.join(self.logs_dir, f'{session_name}',
                                                      f'session_{session_name}_speaker_transcription.json')
        segments_dir = os.path.join(self.audio_segments_dir, session_name)
        visualization_dir = os.path.join(self.visualizations_dir, f'session_{session_name}')
        os.makedirs(visualization_dir, exist_ok=True)

        segments_path_list = sorted(
            [os.path.join(segments_dir, file) for file in os.listdir(segments_dir)],
            key=lambda x: int(os.path.basename(x).split('_')[-1][:-4])
        )

        start_time = datetime.now()  # starting datetime object of the conversation
        time = timedelta(seconds=0)
        segment_no = 0
        speaker_recognition_log_entries = []

        with tqdm(total=len(segments_path_list), desc=f"Processing segments for {session_name}",
                  unit="segment", position=0, leave=True) as pbar:
            for segment_path in segments_path_list:
                assert isinstance(segment_path, str), "segment_path must be a string"
                if segment_path.endswith('.DS_Store'):
                    continue
                time += timedelta(seconds=self.segment_duration)
                segment_start_time = int((start_time + time).timestamp())
                speakers, similarities, durations = [], [], []
                processed_segment_path = self.recorder.post_processing(segment_path, sampling_rate=16000, inplace=True)

                if processed_segment_path:
                    resample(segment_path, 8000)
                    result = self.separator(segment_path)

                    for i, signal in enumerate(result['output_pcm_list']):
                        save_file = f'{segment_path[:-4]}_spk{i}.wav'
                        sf.write(save_file, np.frombuffer(signal, dtype=np.int16), 8000)

                        # speaker recognition on separated signals
                        processed_save_file = self.recorder.apply_vad(save_file, sampling_rate=8000, inplace=False)
                        speaker = 'unknown' if processed_save_file else 'silent'
                        duration = self.segment_duration
                        similarity = 0

                        if processed_save_file:
                            duration = self.calculate_audio_duration(save_file)
                            normalize_rms(save_file, rms_level=-20)
                            name, similarity = self.recognizer.recognize(save_file)

                            if similarity > self.threshold:
                                speaker = name

                        speakers.append(speaker)
                        similarities.append(np.round(np.float64(similarity), 4))
                        durations.append(duration)
                else:
                    speakers.append('silent')
                    similarities.append(0)
                    durations.append(self.segment_duration)

                final_speakers, final_similarities, final_durations = self._post_process_results(speakers, similarities,
                                                                                                 durations)
                speaker_recognition_log_entries.append(
                    self.speaker_recognition_results(segment_no, segment_start_time, final_speakers, final_similarities,
                                                     final_durations))
                segment_no += 1
                pbar.update()

        # Write all speaker_recognition_log_entries to the JSON file at once
        with open(speaker_recognition_log_path, 'w') as f:
            json.dump(speaker_recognition_log_entries, f, indent=5)

        # Visualize the speaker recognition results
        plot_speaking_interaction_network(speaker_recognition_log_path, visualization_dir)
        plot_speaker_diarization_interactive(speaker_recognition_log_path, visualization_dir)

        # Aggregate segments into chunks and transcribe them
        chunk_list = self._aggregate_segments_by_speaker(speaker_recognition_log_path)
        formatted_audio_file_path = os.path.join(self.audio_formatted_dir, f'{session_name}_formatted.wav')
        speaker_transcription_log_entries = self._transcribe_by_chunks(formatted_audio_file_path, chunk_list,
                                                                       session_name)

        with open(speaker_transcription_log_path, 'w') as f:
            json.dump(speaker_transcription_log_entries, f, indent=5)

        convert_transcription_json_to_txt(speaker_transcription_log_path)

    def _aggregate_segments_by_speaker(self, speaker_recognition_log_path):
        with open(speaker_recognition_log_path, 'r') as file:
            speaker_recognition_log = json.load(file)

        speakers_segments = {}  # Dictionary to hold the current speaker segments
        chunk_list = []
        for entry in speaker_recognition_log:
            segment_start_time = entry['segment_start_time']
            segment_end_time = segment_start_time + self.segment_duration
            speakers = json.loads(entry['speakers'])

            # Update existing speakers' end time and add new speakers
            for speaker in speakers:
                if speaker in speakers_segments:
                    speakers_segments[speaker][1] = segment_end_time
                else:
                    speakers_segments[speaker] = [segment_start_time, segment_end_time]

            # Check for speakers who are not in the current segment
            for speaker in list(speakers_segments.keys()):
                if speaker not in speakers:
                    # Update the end time for this speaker and then remove from the dictionary
                    speakers_segments[speaker][1] = segment_start_time
                    chunk_list.append((speaker, [speakers_segments[speaker][0], speakers_segments[speaker][1]]))
                    del speakers_segments[speaker]

        # Handle the last segment for remaining speakers
        if speaker_recognition_log:
            last_segment_start_time = speaker_recognition_log[-1]['segment_start_time']
            last_segment_end_time = last_segment_start_time + self.segment_duration
            for speaker, times in speakers_segments.items():
                times[1] = last_segment_end_time
                chunk_list.append((speaker, times))

        return chunk_list

    def _transcribe_by_chunks(self, audio_path, chunk_list, session_name):
        """Given a chunk list, transcribe the audio by chunk"""
        chunk_dir = os.path.join(self.audio_chunks_dir, session_name)
        if os.path.exists(chunk_dir):
            shutil.rmtree(chunk_dir)
        os.makedirs(chunk_dir)

        entries = []
        if self.tr:
            audio_start_time = chunk_list[0][1][0]
            with tqdm(total=len(chunk_list), desc=f"Processing aggregated segments chunk",
                      unit="chunk", position=0, leave=True) as pbar:
                for index, chunk in enumerate(chunk_list):
                    speaker = chunk[0]
                    chunk_start_time = chunk[1][0]
                    chunk_end_time = chunk[1][1]

                    # start_offset = chunk_start_time - audio_start_time
                    # end_offset = chunk_end_time - audio_start_time
                    # text = self.transcriber.transcribe(audio_path, start_time=start_offset, end_time=end_offset)
                    # if speaker != 'silent' else ''

                    start_offset_ms = 1000 * (chunk_start_time - audio_start_time)
                    end_offset_ms = 1000 * (chunk_end_time - audio_start_time)
                    chunk_path = os.path.join(chunk_dir, f'chunk_{index}_{speaker}.wav')
                    crop_and_concatenate_wav(audio_path, [(start_offset_ms, end_offset_ms)], chunk_path)
                    self.recorder.apply_nr(chunk_path)
                    normalize_rms(chunk_path, rms_level=-20)
                    text = self.transcriber.transcribe(chunk_path) if speaker != 'silent' else ''
                    transcription_entry = {
                        "chunk_no": index,
                        "chunk_start_time": chunk_start_time,
                        "chunk_end_time": chunk_end_time,
                        "speaker": speaker,
                        "text": text,
                    }
                    print(transcription_entry)
                    entries.append(transcription_entry)
                    pbar.update()

        return entries

    def _transcribe_segment(self, audio_path, speaker, segment_no, segment_start_time):
        if self.tr:
            text = self.transcriber.transcribe(audio_path)
            transcription_entry = {
                "segment_no": segment_no,
                "segment_start_time": segment_start_time,
                "speakers": json.dumps([speaker]),
                "text": text,
            }
            return transcription_entry

    def _post_process_results(self, speakers, similarities, durations):
        """Post-process the recognition results of separated signals to handle edge cases."""
        # If there's only one speaker, keep it as is
        if len(speakers) == 1:
            return speakers, similarities, durations

        # If both speakers are the same, keep the one with the highest similarity
        if speakers[0] == speakers[1]:
            max_similarity_index = 0 if similarities[0] > similarities[1] else 1
            return [speakers[max_similarity_index]], [similarities[max_similarity_index]], [
                durations[max_similarity_index]]

        # If both are real speakers, keep them as is
        if all(speaker not in ['silent', 'unknown'] for speaker in speakers):
            return speakers, similarities, durations

        # If there's at least one real speaker, keep only the real ones
        real_speakers, real_similarities, real_durations = self.filter_real_speakers(speakers, similarities, durations)
        if real_speakers:
            return real_speakers, real_similarities, real_durations

        # Special cases for 'silent' and 'unknown'
        if 'unknown' in speakers and 'silent' in speakers:
            return ['unknown'], [similarities[speakers.index('unknown')]], [durations[speakers.index('unknown')]]
        if speakers.count('silent') == 2:
            return ['silent'], [similarities[0]], [durations[0]]
        if speakers.count('unknown') == 2:
            return ['unknown'], [max(similarities)], [max(durations)]

        return [], [], []

    @staticmethod
    def calculate_audio_duration(audio_path):
        with sf.SoundFile(audio_path) as f:
            return len(f) / f.samplerate

    @staticmethod
    def filter_real_speakers(speakers, similarities, durations):
        """Filter out 'silent' and 'unknown' from speakers and their associated similarities and durations."""
        real_speakers = []
        real_similarities = []
        real_durations = []
        for i, speaker in enumerate(speakers):
            if speaker not in ['silent', 'unknown']:
                real_speakers.append(speaker)
                real_similarities.append(similarities[i])
                real_durations.append(durations[i])

        return real_speakers, real_similarities, real_durations

    @staticmethod
    def speaker_recognition_results(segment_no, segment_start_time, final_speakers=None,
                                    final_similarities=None, final_durations=None, ):
        """Log and upload the recognition results."""
        recognition_entry = {
            "segment_no": segment_no,
            "segment_start_time": segment_start_time,
            "speakers": json.dumps(final_speakers),
            "similarities": json.dumps(final_similarities),
            "durations": json.dumps(final_durations),
        }
        return recognition_entry

    @staticmethod
    def identify_speaker_change_borders(chunk_list):
        """Note: this function only applicable to normal processing, without sp"""
        borders = []
        start_time = chunk_list[0][1][0]
        for i in range(1, len(chunk_list)):
            if chunk_list[i][0] != chunk_list[i - 1][0]:  # Speaker change detected
                border_time = chunk_list[i][1][0] - start_time  # Time offset from the start of the conversation
                candidates = [chunk_list[i - 1][0], chunk_list[i][0]]
                borders.append((border_time, candidates))

        return borders

    @staticmethod
    def update_chunk_list(chunk_list, border_index, left_speaker, right_speaker, segment_half_duration):
        left_chunk_speaker = chunk_list[border_index][0]
        right_chunk_speaker = chunk_list[border_index + 1][0]

        first_start_time = chunk_list[border_index][1][0]
        first_end_time = chunk_list[border_index][1][1] - segment_half_duration
        second_start_time = first_end_time
        second_end_time = chunk_list[border_index][1][1]
        third_start_time = second_end_time
        third_end_time = chunk_list[border_index + 1][1][0] + segment_half_duration
        fourth_start_time = third_end_time
        fourth_end_time = chunk_list[border_index + 1][1][1]

        chunk_list[border_index] = (left_chunk_speaker, (first_start_time, first_end_time))
        new_chunk_left = (left_speaker, (second_start_time, second_end_time))
        chunk_list.insert(border_index + 1, new_chunk_left)
        new_chunk_right = (right_speaker, (third_start_time, third_end_time))
        chunk_list.insert(border_index + 2, new_chunk_right)
        chunk_list[border_index + 3] = (right_chunk_speaker, (fourth_start_time, fourth_end_time))

        return 2

    @staticmethod
    def aggregate_chunks(chunk_list):
        aggregated_chunks = []
        current_speaker = None
        current_start_time = None
        current_end_time = None

        for speaker, (start_time, end_time) in chunk_list:
            # Skip chunks with identical start and end times
            if start_time == end_time:
                continue

            # If the current speaker is the same as the last, extend the current chunk
            if speaker == current_speaker:
                current_end_time = end_time
            else:
                # If there's a current chunk, add it to the aggregated list
                if current_speaker is not None:
                    aggregated_chunks.append((current_speaker, (current_start_time, current_end_time)))

                # Start a new chunk
                current_speaker = speaker
                current_start_time = start_time
                current_end_time = end_time

        # Add the last chunk if it exists
        if current_speaker is not None:
            aggregated_chunks.append((current_speaker, (current_start_time, current_end_time)))

        return aggregated_chunks

import configparser
import gc
import json
import logging
import os
import threading
import time

from src._enum import BLUE, ENDC
from src.utils.influx_client import InfluxDBClientWrapper
from src.utils.input_utils import get_bucket_name, get_number_of_group_members, get_function_synchronizer
from src.utils.analyze_utils import session_analysis_audio
from src.utils.logger_utils import get_logger
from src.utils.mqtt_client import MQTTClientWrapper
from src.utils.os_utils import clear_directory
from src.utils.redis_client import RedisClientWrapper
from src.utils.thread_utils import RaisingThread


class Synchronizer:
    """The synchronizer synchronizes speaker recognition results from audio bases among the same session."""
    logger = get_logger('synchronizer')

    def __init__(self, base_type: str, root_dir: str = None, config_path: str = None, dominant: bool = False,
                 sp: bool = False):
        """ Initialize the synchronizer object.

        :param base_type:  the audio base type
        :param root_dir: root directory of the project
        :param config_path: path to the configuration file
        :param dominant: Whether select the dominant speaker or not
        :param sp:  Tag of speech separation
        """
        self.base_type = base_type.capitalize()
        self.root_dir = root_dir if root_dir else os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        self.config_path = os.path.join(self.root_dir, config_path if config_path else 'conf/audio_base.ini')
        self.dominant = dominant

        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        self.audio_temp_dir = os.path.join(self.root_dir, 'audio', 'temp')
        self.logger_dir = os.path.join(self.root_dir, 'logger')

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.result_expiry_time = int(
            self.config['Synchronizer']['result_expiry_time'])  # Expiry time of retained results
        self.time_range = int(self.config[self.base_type]['recognize_sp_duration']) if sp else int(
            self.config[self.base_type]['recognize_duration'])  # Time range for finding the closest segment
        self.redis_client = RedisClientWrapper(self.config_path)  # Redis wrapped client
        self.mqtt_client = MQTTClientWrapper(self.config_path)  # MQTT wrapped client
        self.influx_client = InfluxDBClientWrapper(self.config_path)  # InfluxDB wrapped client

        self.bucket_name = None  # Session bucket name
        self.number_of_speaker = None  # Number of group members
        self.latest_time = None  # Record start time of the most recent synchronized segment
        self.retained_results = None  # Results to be handled {time: {id: {'speaker':x, 'similarity':x, 'duration':x}}}
        self.threads = []  # List of thread objects
        self.stop_event = threading.Event()  # Event for stopping all threads

    def run(self):
        """Main menu for the synchronizer."""
        print('\033]0;Audio Synchronizer\007')
        func_map = {1: self._start_synchronizing}

        while True:
            try:
                select_fun = get_function_synchronizer()
                if select_fun == 0:
                    print("------------------------------------------------")
                    clear_directory(os.path.join(self.audio_temp_dir))
                    self.logger.info("Exiting audio synchronizer...")
                    break
                func_map.get(select_fun, lambda: print("Invalid option."))()
            except (Exception, KeyboardInterrupt) as e:
                self.logger.warning(
                    f"\nDuring running synchronizer, catch: {'KeyboardInterrupt' if isinstance(e, KeyboardInterrupt) else e}, Come back to the main menu.",
                    exc_info=True)

    def _start_synchronizing(self):
        """Start the synchronization process."""
        self.bucket_name = get_bucket_name(self.influx_client)
        self.number_of_speaker = get_number_of_group_members()
        self.latest_time = 0
        self.retained_results = {}
        self.logger = get_logger(f'synchronizer-{self.bucket_name}',
                                 os.path.join(self.logger_dir, f'{self.bucket_name}_synchronizer.log'),
                                 level=logging.DEBUG, console_level=logging.INFO, file_level=logging.DEBUG)
        self.mqtt_client.reinitialise(on_message=self._handle_base_result, topics=f'{self.bucket_name}/audio')
        self.mqtt_client.loop_start()

        # Create threads
        self._create_thread(self._send_start_regularly)
        self._create_thread(self._listen_for_stop_signal)

        # Start threads
        exception_occurred = None
        try:
            self._start_threads()
            self._join_threads()
        except (Exception, KeyboardInterrupt) as e:
            self.logger.warning(
                f"\nDuring synchronization, catch: {'KeyboardInterrupt' if isinstance(e, KeyboardInterrupt) else e}",
                exc_info=True)
            exception_occurred = e
        finally:
            self._synchronization_handler(exception_occurred)

    def _synchronization_handler(self, e):
        """Handle exceptions and stop all threads."""
        if e:
            self._stop_threads()
        else:
            self.logger.info("All threads stopped.")

        self.mqtt_client.loop_stop()
        self.redis_client.publish(f"{self.bucket_name}/control", 'STOP')  # send STOP command to all bases
        session_analysis_audio(self.bucket_name, self.influx_client)
        clear_directory(self.audio_temp_dir)
        self._clean_up()

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
                    self.logger.warning(f"During the thread stopping, catch: {e}", exc_info=True)
        self.threads.clear()

    def _clean_up(self):
        """Free memory by resetting dictionaries."""
        self.bucket_name = None
        self.number_of_speaker = None
        self.latest_time = None
        self.retained_results = None
        gc.collect()

    def _send_start_regularly(self):
        """Send the START signal to all bases regularly."""
        while not self.stop_event.is_set():
            self.redis_client.publish(f"{self.bucket_name}/control", 'START')
            time.sleep(self.time_range)

    def _listen_for_stop_signal(self):
        """Listen on the redis bucket control channel for the STOP signal."""
        p = self.redis_client.subscribe(f"{self.bucket_name}/control")
        self.logger.info("Listening for STOP signal...")

        while not self.stop_event.is_set():
            message = p.get_message()
            if message and message['data'] == b'STOP':
                self.logger.info("Received STOP signal, stop synchronizing...")
                self._stop_threads()

    # def _find_closest_segment(self, current_time):
    #     time_differences = {key: abs(current_time - key) for key in self.retained_results.keys()}
    #     valid_segments = {key: diff for key, diff in time_differences.items() if diff <= self.time_range}
    #     closest_segment = min(valid_segments.keys(), default=None)
    #     return closest_segment

    def _find_closest_segment(self, current_time, base_id):
        """Find the closest segment of the current received segment among the retained results."""
        # Calculate time differences for all segments in retained results
        time_differences = {key: abs(current_time - key) for key in self.retained_results.keys()}

        # Filter valid segments based on time difference and exclude segments where base_id already exists
        valid_segments = {
            key: diff for key, diff in time_differences.items()
            if diff <= self.time_range and base_id not in self.retained_results[key]
        }

        # If no valid segments are found, return None
        if not valid_segments:
            return None

        # Choose the segment with the earliest segment time
        closest_segment = min(valid_segments.keys())

        # Choose the segment with the closest segment time
        # closest_segment = min(valid_segments, key=valid_segments.get)

        return closest_segment

    # def _update_time(self, latest_time, record_start_time):
    #     n = (record_start_time - latest_time) // self.time_range
    #     updated_latest_time = latest_time + self.time_range * n
    #     if record_start_time - updated_latest_time >= self.time_range / 2:
    #         updated_latest_time += self.time_range
    #     return updated_latest_time

    def _handle_base_result(self, client, userdata, message):
        """Handle the received speaker recognition result from the base."""
        new_base_result = json.loads(message.payload.decode('utf-8'))
        record_start_time = float(new_base_result['record_start_time'])

        if not self.latest_time:
            self.latest_time = int(record_start_time)
            self.retained_results[self.latest_time] = {}
            self._update_retained_results(self.latest_time, new_base_result)
            return

        expired_keys = [key for key in self.retained_results.keys() if
                        record_start_time - key > self.result_expiry_time]

        for key in expired_keys:
            consolidated_result = self._consolidate_results(self.retained_results[key])
            consolidated_result['segment_start_time'] = key
            self.logger.debug(f"\033[91mExpired key {key} with result {self.retained_results[key]}\033[0m")
            self._log_and_upload_results(consolidated_result)
            del self.retained_results[key]

        closest_segment = self._find_closest_segment(record_start_time, new_base_result['base_id'])
        if closest_segment is None:
            if self.latest_time > record_start_time:  # outdated message
                self.logger.debug(
                    f"\033[91m{new_base_result['base_id']} results is outdated, record time is {record_start_time}\033[0m")
                return
            else:
                # self.latest_time = self._update_time(self.latest_time, record_start_time)
                # self.latest_time += self.time_range
                self.latest_time = record_start_time  # Update latest time to the record start time
                self.retained_results[self.latest_time] = {}
                self._update_retained_results(self.latest_time, new_base_result)
        else:
            self._update_retained_results(closest_segment, new_base_result)

        segment_time = closest_segment if closest_segment else self.latest_time
        self.logger.debug(
            f"Segment {segment_time} is selected for {new_base_result['base_id']} record time is {record_start_time}")
        if len(self.retained_results[segment_time]) == self.number_of_speaker:
            consolidated_result = self._consolidate_results(self.retained_results[segment_time])
            consolidated_result['segment_start_time'] = segment_time
            self._log_and_upload_results(consolidated_result)
            del self.retained_results[segment_time]

    def _update_retained_results(self, segment_time, latest_base_result):
        """Helper function to update or add the recognition result of one segment sent from base"""
        if latest_base_result['base_id'] in self.retained_results[segment_time]:
            self.logger.debug(
                f"\033[91mOverwrite results: {self.retained_results[segment_time][latest_base_result['base_id']]}\033[0m")
        self.retained_results[segment_time][latest_base_result['base_id']] = {
            'record_start_time': latest_base_result['record_start_time'],
            'speakers': json.loads(latest_base_result['speakers']),
            'similarities': json.loads(latest_base_result['similarities']),
            'durations': json.loads(latest_base_result['durations']),
        }

    def _consolidate_results(self, segment_results):
        """Consolidate the results dictionary of one segment, keys are base id, values are base results."""
        speakers, similarities, durations, record_start_times = [], [], [], []
        if self.dominant:
            best_result, i = self.find_best_result(segment_results)
            record_start_times.append(best_result['record_start_time'])
            speakers.append(best_result['speakers'][i])
            similarities.append(best_result['similarities'][i])
            durations.append(best_result['durations'][i])
        else:
            for res in segment_results.values():
                # Append real speakers
                for i, speaker in enumerate(res['speakers']):
                    if speaker not in ['unknown', 'silent']:
                        record_start_times.append(res['record_start_time'])
                        speakers.append(res['speakers'][i])
                        similarities.append(res['similarities'][i])
                        durations.append(res['durations'][i])
            if not speakers:
                best_result, i = self.find_best_result(segment_results)
                record_start_times.append(best_result['record_start_time'])
                speakers.append(best_result['speakers'][i])
                similarities.append(best_result['similarities'][i])
                durations.append(best_result['durations'][i])

        return {'speakers': speakers, 'similarities': similarities, 'record_start_times': record_start_times,
                'durations': durations}

    def _log_and_upload_results(self, consolidated_result):
        """Log and upload consolidated results to InfluxDB"""
        recognition_data = {
            "measurement": "speaker recognition",
            "fields": {
                "segment_start_time": float(consolidated_result['segment_start_time']),
                "speakers": json.dumps(consolidated_result['speakers']),
                "similarities": json.dumps(consolidated_result['similarities']),
                "record_start_times": json.dumps(consolidated_result['record_start_times']),
                "durations": json.dumps(consolidated_result['durations'])
            },
        }
        print(f"{BLUE}[Speaker Recognition]{ENDC}{recognition_data['fields']['segment_start_time']}: "
              f"{BLUE}{recognition_data['fields']['speakers']}{ENDC}, "
              f"similarity: {recognition_data['fields']['similarities']}")
        self.influx_client.write(self.bucket_name, recognition_data)

    @staticmethod
    def find_best_result(segment_results: dict):
        """Find the best result among the segment results."""
        best_result = None
        max_similarity = -2
        max_index = -1

        for result in segment_results.values():
            current_index, current_similarity = max(enumerate(result["similarities"]), key=lambda x: x[1])
            if current_similarity > max_similarity:
                best_result = result
                max_similarity = current_similarity
                max_index = current_index

        return best_result, max_index

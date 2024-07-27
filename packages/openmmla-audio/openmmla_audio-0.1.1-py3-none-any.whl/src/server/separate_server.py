"""
-Description: Speech separation server separates the audio signals from a mixed signal. It receives audio signal from
base station, and sends back two separated signals. It can help to differentiate a speaker's voice from an overlapped
speaking environment.
"""
import base64
import configparser
import gc
import os
import sys

import torch
from flask import Flask, request, jsonify
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import write_frames_to_file
from src.utils.logger_utils import get_logger

app = Flask(__name__)
config = configparser.ConfigParser()
config_path = os.path.join(root_dir, 'conf', 'audio_base.ini')
config.read(config_path)
logger = get_logger('modelscope', os.path.join(root_dir, 'logger', 'separate_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)

use_cuda = True
device = 'gpu' if use_cuda and torch.cuda.is_available() else 'cpu'
sp_model = config['Server']['sp_model']
sp_model_local = config['Server']['sp_model_local']

# Initialize speech separation model
try:
    separation_model = pipeline(Tasks.speech_separation, device=device, model=sp_model)
except ValueError:
    separation_model = pipeline(Tasks.speech_separation, device=device, model=sp_model_local)


@app.route('/separate', methods=['POST'])
def separate_speech():
    if request.files:
        try:
            base_id = request.values.get('base_id')
            audio_file = request.files['audio']
            audio_file_path = os.path.join(server_file_folder, f'separate_audio_{base_id}.wav')
            write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, 8000)

            result = separation_model(audio_file_path)
            processed_bytes_streams = []

            for signal in result['output_pcm_list']:
                encoded_bytes_stream = base64.b64encode(signal).decode('utf-8')
                processed_bytes_streams.append(encoded_bytes_stream)

            # Return the processed audio data
            return jsonify({"processed_bytes_streams": processed_bytes_streams}), 200
        except Exception as e:
            logger.error(f"during speech separation, {e} happens.")
            return jsonify({"error": str(e)}), 500
        finally:
            torch.cuda.empty_cache()
            gc.collect()
    else:
        return jsonify({"error": "No audio file provided"}), 400


# gunicorn -w 1 -b 0.0.0.0:5001 separate_server:app
# hypercorn -w 1 -b 0.0.0.0:5001 separate_server:app
# kill -9 $(lsof -ti:5001)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

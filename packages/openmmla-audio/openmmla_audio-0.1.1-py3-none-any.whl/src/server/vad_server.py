"""
-Description: VAD server detects the speaker's voice activity. It receives audio signal from base station and sends back
the detected voice signal.
"""
import gc
import io
import os
import sys
from typing import Union

import torch
from flask import Flask, request, jsonify, send_file

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import write_frames_to_file
from src.utils.logger_utils import get_logger

app = Flask(__name__)
logger = get_logger('silero', os.path.join(root_dir, 'logger', 'vad_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)

use_cuda = True
use_onnx = True
cuda_enable = use_cuda and torch.cuda.is_available()

# Initialize VAD
torch.set_num_threads(1)
try:
    vad_model, utils = torch.hub.load(
        repo_or_dir='snakers4/silero-vad', model='silero_vad', force_reload=True, onnx=use_onnx)
except Exception:
    vad_model, utils = torch.hub.load(
        repo_or_dir=os.path.join(root_dir, 'src/utils/silero-vad'),
        model='silero_vad', source='local', force_reload=True, onnx=use_onnx)

(get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils


def apply_vad(input_path: str, sampling_rate: int, inplace: int) -> Union[str, None]:
    wav = read_audio(input_path, sampling_rate=sampling_rate)
    speech_timestamps = get_speech_timestamps(wav, vad_model, sampling_rate=sampling_rate)
    if not speech_timestamps:
        return None
    if inplace:
        save_audio(input_path, collect_chunks(speech_timestamps, wav), sampling_rate=sampling_rate)
    if cuda_enable:
        torch.cuda.empty_cache()
    return input_path


@app.route('/vad', methods=['POST'])
def vad():
    try:
        base_id = request.values.get('base_id')
        fr = int(request.values.get('fr', 16000))
        inplace = int(request.values.get('inplace', 0))
        audio_file = request.files['audio']
        audio_file_path = os.path.join(server_file_folder, f'vad_audio_{base_id}.wav')
        write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, fr)

        logger.info(f"starting VAD for {base_id}...")
        result = apply_vad(audio_file_path, fr, inplace)
        logger.info(f"finished VAD for {base_id}.")

        if inplace and result:
            with open(result, 'rb') as f:
                audio_data = f.read()
            return send_file(io.BytesIO(audio_data), mimetype="audio/wav"), 200
        else:
            # For cases where inplace is False or speech timestamps are not detected
            return jsonify({"result": result or "None"}), 200

    except Exception as e:
        logger.error(f"Error processing VAD for {base_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        torch.cuda.empty_cache()
        gc.collect()


# gunicorn -w 1 -b 0.0.0.0:5004 vad_server:app
# hypercorn -w 1 -b 0.0.0.0:5004 vad_server:app
# kill -9 $(lsof -ti:5004)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, threaded=True)

"""
-Description: Resample server receives audio signals from audio base stations, and then resample them and send it back.
"""
import gc
import io
import os
import sys

from flask import Flask, request, jsonify, send_file

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import resample, write_frames_to_file
from src.utils.logger_utils import get_logger

app = Flask(__name__)
logger = get_logger('resampler', os.path.join(root_dir, 'logger', 'resample_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)


@app.route('/resample', methods=['POST'])
def resample_audio():
    if request.files:
        try:
            base_id = request.values.get('base_id')
            fr = int(request.values.get('fr'))
            target_fr = int(request.values.get('target_fr'))
            audio_file = request.files['audio']
            audio_file_path = os.path.join(server_file_folder, f'resample_audio_{base_id}.wav')
            write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, fr)

            logger.info(f"starting resampling for {base_id}...")
            resample(audio_file_path, target_fr)
            logger.info(f"finished resampling for {base_id}...")

            with open(audio_file_path, 'rb') as f:
                audio_data = f.read()
            return send_file(io.BytesIO(audio_data), mimetype="audio/wav"), 200
        except Exception as e:
            logger.error(f"during resampling, {e} happens.")
            return jsonify({"error": str(e)}), 500
        finally:
            gc.collect()
    else:
        return jsonify({"error": "No audio file provided"}), 400


# gunicorn -w 1 -b 0.0.0.0:5005 resample_server:app
# hypercorn -w 1 -b 0.0.0.0:5005 resample_server:app
# kill -9 $(lsof -ti:5005)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

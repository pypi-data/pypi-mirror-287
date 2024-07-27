"""
-Description: Infer server generates the embeddings from audio signal in latent space. It receives audio signal from
node base, and sends back the embeddings.
"""
import configparser
import gc
import json
import os
import sys

import nemo.collections.asr as nemo_asr
import torch
from flask import Flask, request, jsonify

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import write_frames_to_file
from src.utils.logger_utils import get_logger

app = Flask(__name__)
config = configparser.ConfigParser()
config_path = os.path.join(root_dir, 'conf', 'audio_base.ini')
config.read(config_path)
logger = get_logger('titanet', os.path.join(root_dir, 'logger', 'infer_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)

use_cuda = True
sr_model = config['Server']['sr_model']

# Initialize titanet model
if use_cuda:
    infer_model = nemo_asr.models.EncDecSpeakerLabelModel.from_pretrained(model_name=sr_model)
else:
    infer_model = nemo_asr.models.EncDecSpeakerLabelModel.from_pretrained(model_name=sr_model, map_location='cpu')
infer_model.eval()


@app.route('/infer', methods=['POST'])
def infer():
    if request.files:
        try:
            base_id = request.values.get('base_id')
            fr = int(request.values.get('fr'))
            audio_file = request.files['audio']
            audio_file_path = os.path.join(server_file_folder, f'infer_audio_{base_id}.wav')
            write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, fr)

            logger.info(f"starting inference for {base_id}...")
            feature = infer_model.get_embedding(audio_file_path)
            embeddings = json.dumps(feature.cpu().numpy().tolist())
            logger.info(f"finished inference for {base_id}.")

            return jsonify({"embeddings": embeddings}), 200
        except Exception as e:
            logger.error(f"during inference, {e} happens.")
            return jsonify({"error": str(e)}), 500
        finally:
            torch.cuda.empty_cache()
            gc.collect()
    else:
        return jsonify({"error": "No audio file provided"}), 400


# gunicorn -w 1 -b 0.0.0.0:5002 infer_server:app
# hypercorn -w 1 -b 0.0.0.0:5002 infer_server:app
# kill -9 $(lsof -ti:5002)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

"""
-Description: Speech enhancement server enhance the audio signal. It receives audio signal from node
base and sends back the enhanced signal.
"""
import gc
import io
import math
import os
import sys

import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio
from flask import Flask, request, jsonify, send_file

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import write_frames_to_file
from src.utils.logger_utils import get_logger

app = Flask(__name__)
logger = get_logger('denoiser', os.path.join(root_dir, 'logger', 'enhance_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)

use_cuda = True

# Initialize denoiser
cuda_enable = use_cuda and torch.cuda.is_available()
nr_model = pretrained.dns64().cuda() if cuda_enable else pretrained.dns64()


def apply_nr(input_path: str) -> str:
    chunk_size = 30
    sr = torchaudio.info(input_path).sample_rate
    total_duration = torchaudio.info(input_path).num_frames / sr
    output_chunks = []

    if total_duration == 0:
        raise ValueError("Total duration of the audio is zero.")

    try:
        for start in range(0, math.ceil(total_duration), chunk_size):
            chunk, _ = torchaudio.load(input_path, num_frames=int(chunk_size * sr), frame_offset=int(start * sr))
            if chunk.nelement() == 0:
                continue  # Skip empty chunks

            if cuda_enable:
                chunk = chunk.cuda()
            chunk = convert_audio(chunk, sr, nr_model.sample_rate, nr_model.chin)

            with torch.no_grad():
                denoised_chunk = nr_model(chunk[None])[0]
            output_chunks.append(denoised_chunk.cpu())

            if cuda_enable:
                torch.cuda.empty_cache()

        if not output_chunks:
            raise RuntimeError("No chunks were processed. Check the audio file and processing steps.")

        processed_audio = torch.cat(output_chunks, dim=1)  # Concatenate and save the processed chunks
        torchaudio.save(input_path, processed_audio, sample_rate=nr_model.sample_rate, bits_per_sample=16)
    except Exception as e:
        raise RuntimeError(f"Error in apply_nr: {e}")
    finally:
        torch.cuda.empty_cache()
        gc.collect()

    return input_path


@app.route('/enhance', methods=['POST'])
def enhance_audio():
    try:
        base_id = request.values.get('base_id')
        fr = int(request.values.get('fr', 16000))
        audio_file = request.files['audio']
        audio_file_path = os.path.join(server_file_folder, f'enhance_audio_{base_id}.wav')
        write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, fr)

        logger.info(f"starting enhancement for {base_id}...")
        apply_nr(audio_file_path)
        logger.info(f"finished enhancement for {base_id}.")

        with open(audio_file_path, 'rb') as f:
            audio_data = f.read()

        return send_file(
            io.BytesIO(audio_data),
            mimetype="audio/wav"
        )
    except Exception as e:
        logger.error(f"during enhancement, {e} happens.")
        return jsonify({"error": str(e)}), 500
    finally:
        torch.cuda.empty_cache()
        gc.collect()


# gunicorn -w 1 -b 0.0.0.0:5003 enhance_server:app
# hypercorn -w 1 -b 0.0.0.0:5003 enhance_server:app
# kill -9 $(lsof -ti:5003)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, threaded=True)

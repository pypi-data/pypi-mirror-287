"""
-Description: Speech transcription server transcribe the audio signal into speech. It receives audio signal from base
station and sends back transcription text.
"""
import configparser
import gc
import math
import os
import sys
import threading

import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio
from flask import Flask, request, jsonify

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
sys.path.append(root_dir)

from src.utils.audio_utils import write_frames_to_file
from src.utils.auga import normalize_rms
from src.utils.logger_utils import get_logger
from src.utils.transcriber import Transcriber

app = Flask(__name__)
config = configparser.ConfigParser()
config_path = os.path.join(root_dir, 'conf', 'audio_base.ini')
config.read(config_path)
logger = get_logger('whisper', os.path.join(root_dir, 'logger', 'transcribe_server.log'))
server_file_folder = os.path.join(root_dir, 'src/server/temp')
os.makedirs(server_file_folder, exist_ok=True)

use_cuda = False
cuda_enable = use_cuda and torch.cuda.is_available()
tr_model = config['Server']['tr_model']
language = config['Server']['language']

# Initialize denoiser and transcriber
nr_model = pretrained.dns64().cuda() if cuda_enable else pretrained.dns64()
transcriber = Transcriber(tr_model, language=language, use_cuda=use_cuda)
transcriber_lock = threading.Lock()


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


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        with transcriber_lock:  # Acquire lock
            base_id = request.values.get('base_id')
            fr = int(request.values.get('fr', 16000))
            audio_file = request.files['audio']
            audio_file_path = os.path.join(server_file_folder, f'transcribe_audio_{base_id}.wav')
            write_frames_to_file(audio_file_path, audio_file.read(), 1, 2, fr)

            logger.info(f"starting transcribe for {base_id}...")
            if fr == 16000:
                apply_nr(audio_file_path)
            normalize_rms(infile=audio_file_path, rms_level=-20)
            text = transcriber.transcribe(audio_file_path)
            logger.info(f"finished transcribe for {base_id}.")

        return jsonify({"text": text}), 200
    except Exception as e:
        logger.error(f"during transcribing, {e} happens.")
        return jsonify({"error": str(e)}), 500
    finally:
        torch.cuda.empty_cache()
        gc.collect()


# gunicorn -w 1 -b 0.0.0.0:5000 transcribe_server:app
# hypercorn -w 1 -b 0.0.0.0:5000 transcribe_server:app
# kill -9 $(lsof -ti:5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

import json
import os

from tqdm import tqdm

from src.utils.transcriber import Transcriber


# Post-processing of transcription on session
def transcribe_session(session_name: str, model_name: str, language: str, device: str):
    session_path = os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), "../audio/real-time",
                                session_name)
    # Check if path is a directory
    if not os.path.isdir(session_path):
        print(f"{session_path} is not a directory.")
        return

    # Get list of subdirectories under session_path
    sub_dirs = [d for d in os.listdir(session_path) if os.path.isdir(os.path.join(session_path, d))]

    # Initialize whisper model
    model = Transcriber(model_name=model_name, language=language, device=device)

    for audio_dir in tqdm(sub_dirs, desc="Processing speaker's conversation", unit='conversation'):
        audio_dir_path = os.path.join(session_path, audio_dir)

        # Get sorted list of audio files
        files_to_transcribe = sorted(
            [os.path.join(audio_dir_path, file) for file in os.listdir(audio_dir_path)],
            key=lambda x: int(os.path.basename(x).split('_')[-1][:-4])
        )

        entries = []
        with tqdm(total=len(files_to_transcribe), desc=f"Transcribe segments for {audio_dir}",
                  unit="segment", position=0, leave=True) as pbar:
            for file in files_to_transcribe:
                speaker = os.path.basename(file).split('/')[-1].split('_')[0]
                text = ''
                # Only transcribe speaker not unknown and silent
                if speaker not in ['unknown', 'silent']:
                    text = model.transcribe(file)
                entry = {
                    'speaker': speaker,
                    'text': text,
                    'start_time': int(os.path.basename(file).split('_')[-1][:-4]),
                }
                entries.append(entry)
                pbar.update()

        # Construct log file name based on session and audio_dir
        session_name = os.path.basename(session_path)
        log_file_name = f"{session_name}_{audio_dir}_transcription.json"
        log_path = os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), "../logs/", log_file_name)

        # Write all entries to the JSON file
        with open(log_path, 'w') as f:
            json.dump(entries, f, indent=5)


def transcribe():
    transcribe_session("session_2023-08-22T11:25:28Z", model_name="medium.en", language="English", device="cpu")


if __name__ == "__main__":
    transcribe()

import json
import os

from googletrans import Translator

# Initialize the Google Translate API translator
translator = Translator()
root_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), "..", "logs")


def translate_text(text):
    try:
        # Check if text is not null
        if text is not None:
            translated = translator.translate(text, src='auto', dest='en')
            return translated.text
        else:
            return None  # return None if original text is None
    except Exception as e:
        print(f"An error occurred: {e}")
        return text  # return original text if translation fails


def translate_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    for entry in json_data:
        original_text = entry.get('text', None)  # use dict.get() to handle missing keys
        print(original_text)
        translated_text = translate_text(original_text)
        print(translated_text)
        entry['text_translated'] = translated_text

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    file_name = "session_2023-09-09T14:21:42Z_speaker_transcription.json"
    file_path = os.path.join(root_dir, file_name)
    translate_json_file(file_path)

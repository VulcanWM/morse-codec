from helpers import text_to_morse, morse_to_audio, audio_to_morse, morse_to_text
from sound import save_file

def encode_file(text, file_name):
    morse = text_to_morse(text)
    audio = morse_to_audio(morse)
    save_file(file_name, audio)

def decode_file(file_name):
    morse = audio_to_morse(file_name)
    text = morse_to_text(morse)
    return text
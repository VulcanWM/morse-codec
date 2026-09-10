from helpers import text_to_morse, morse_to_audio, morse_to_text
from sound import save_file

def encode(text, file_name):
    morse = text_to_morse(text)
    audio = morse_to_audio(morse)
    save_file(file_name, audio)


def decode(file_name):
    # morse = audio_to_morse()
    # morse_to_text(morse)
    return


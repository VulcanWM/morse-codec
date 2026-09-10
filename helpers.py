from sound import silence, tone, UNIT
import numpy as np
from mapping import encode_conversion, decode_conversion

def text_to_morse(text):
    text = text.upper()
    morse = ""
    for char in text:
        morse += encode_conversion[char] + " "
    return morse

def morse_to_text(morse):
    morse_words = morse.strip().split(" ")
    output = ""
    for char_code in morse_words:
        output += decode_conversion[char_code]
    return output

def morse_to_audio(morse):
    audio = []

    symbols = morse.split(" ")

    for symbol in symbols:
        if symbol == "/":
            audio.append(silence(4 * UNIT))
        else:
            for char in symbol:
                if char == ".":
                    audio.append(tone(1 * UNIT))
                else:
                    audio.append(tone(3 * UNIT))
                audio.append(silence(1 * UNIT))
            audio.append(silence(2 * UNIT))

    return np.concatenate(audio)
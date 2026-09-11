from sound import silence, tone, UNIT, load_file
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

def audio_to_morse(file_name):
    sample_rate, audio = load_file(file_name)
    units = int(len(audio) / sample_rate / UNIT)
    samples_per_unit = int(sample_rate * UNIT)
    unit_values = ""
    for i in range(units):
        samples = audio[i*samples_per_unit:(i+1)*samples_per_unit]
        total = 0
        for sample in samples:
            total += abs(int(sample))
        if total == 0:
            unit_values += "0"
        else:
            unit_values += "1"
    unit_values = unit_values.replace("0000000", " / ")
    unit_values = unit_values.replace("000", " ")
    unit_values = unit_values.replace("111", "-")
    unit_values = unit_values.replace("1", ".")
    unit_values = unit_values.replace("0", "")
    return unit_values
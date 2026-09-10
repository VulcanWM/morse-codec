from sound import silence, tone, UNIT
import numpy as np

encode_conversion = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    ".": "/",
}

decode_conversion = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "/": ".",
}

def text_to_morse(text):
    morse = ""
    for char in text:
        morse += encode_conversion[char] + " "
    return morse

def morse_to_text(morse):
    morse_words = morse.split(" ")
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
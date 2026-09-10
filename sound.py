import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100
FREQUENCY = 700
UNIT = 0.1

# dot is 1 unit
# dash is 3 unit
# new letter is 3 unit silence
# 1 unit silence between 2 symbols
# 7 unit silence for end of sentence

def tone(duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * FREQUENCY * t)

    return np.int16(wave * 32767)

def silence(duration):
    return np.zeros(int(SAMPLE_RATE * duration), dtype=np.int16)

def save_file(file_name, audio):
    write(f"${file_name}.wav", SAMPLE_RATE, audio)
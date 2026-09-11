# Morse Codec

This is a simple Python project which can run in the CLI, which:
- encodes text into morse into audio files
- decodes audio files into morse into text

## How it works

Morse Codec converts each character into its corresponding Morse code representation.

The Morse code is then converted into a 700 Hz audio signal using standard Morse timing:
- a dot is 1 unit
- a dash is 3 units
- the gap between symbols is 1 unit
- the gap between letters is 3 units
- the gap between sentences is 7 units

By default, one unit is 0.1 seconds.

When decoding, the audio file is split into units and each unit is classed as either a tone or silence. The lengths of consecutive tones and silences are then used to reconstruct the Morse code and convert it back into text.

## Usage

```bash
pip install -r requirements.txt
```

Encode text into a WAV file:
```
python main.py encode "HELLO" hello.wav
```

Decode a WAV file:
```
python main.py decode hello.wav
```
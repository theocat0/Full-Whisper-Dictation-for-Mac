import sounddevice as sd
import numpy as np
import whisper
import tempfile
import scipy.io.wavfile as wavfile
import time

def main():
    # Initialize Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Model loaded!")

    # Recording parameters
    sample_rate = 16000
    duration = 5  # Record for 5 seconds
    channels = 1

    print("\nPress Enter to start recording (will record for 5 seconds)...")
    input()

    print("Recording...")
    recording = sd.rec(int(duration * sample_rate),
                      samplerate=sample_rate,
                      channels=channels)
    sd.wait()
    print("Recording finished!")

    print("\nTranscribing...")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        wavfile.write(temp_audio.name, sample_rate, recording)
        result = model.transcribe(temp_audio.name)
        print("\nTranscription:", result["text"])

if __name__ == "__main__":
    main() 
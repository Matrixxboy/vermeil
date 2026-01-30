from TTS.api import TTS
import torch
import sounddevice as sd

# Reverting to standard non-cloning model (Tacotron2)
# Using generic English voice as requested
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)

def speak(text):
    audio = tts.tts(text)
    sd.play(audio, samplerate=22050) # Tacotron2 typical rate
    sd.wait()

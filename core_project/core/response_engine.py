from TTS.api import TTS
import torch
import sounddevice as sd

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=torch.cuda.is_available())

def speak(text):
    audio = tts.tts(text)
    sd.play(audio, samplerate=tts.synthesizer.output_sample_rate)
    sd.wait()

import queue
import sounddevice as sd
import vosk
import json
from nlp_processor import recognize_intent

# Set model path
MODEL_PATH = "D:/Project Vermeil AI/vermeil/Core Project/core/vosk_model/vosk-model-small-en-us-0.15"

# Load Vosk model
vosk_model = vosk.Model(MODEL_PATH)

# Create a queue for audio processing
audio_queue = queue.Queue()

# Speech recognition function
def callback(indata, frames, time, status):
    """Callback function to store audio data in queue."""
    if status:
        print(f"Audio Status: {status}")
    audio_queue.put(bytes(indata))

# Configure microphone input
def recognize_speech():
    """Captures microphone input and converts speech to text."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):
        recognizer = vosk.KaldiRecognizer(vosk_model, 16000)

        print("🎤 Listening... Speak now.")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣 Recognized: {text}")
                    return text  # Return recognized speech
                
if __name__ == "main":
    recognize_speech()

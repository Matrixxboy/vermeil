import pvporcupine
import pyaudio
import struct
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv('PICO_VOICE_KEY')

def listen_for_wake_word():
    """ Listens for the wake word and returns True when detected. """
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=["D:/Project Vermeil AI/vermeil/Core Project/core/Wake_Word_model/Hey_Vermeil_v1_0_0.ppn"]
    )

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("Wake word detected! Activating Vermeil AI...")
                return True

    except KeyboardInterrupt:
        print("Stopping...")
    
    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    listen_for_wake_word()


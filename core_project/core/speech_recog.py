import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(timeout=5, phrase_time_limit=None):
    try:
        with sr.Microphone() as source:
            print("\n🎤 Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🗣️ Speak now (listening for pause)...")
            
            # dynamic_energy_threshold=True is default, but explicit setting might help if needed
            # recognizer.pause_threshold = 1.0 # Optional: increase pause threshold
            
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        # Try recognizing speech using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text

        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError as e:
            print(f"🔌 Could not request results from Google Speech Recognition service; {e}")

    except sr.WaitTimeoutError:
        print("⌛ Listening timed out while waiting for speech.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

    return None

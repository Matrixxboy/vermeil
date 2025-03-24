import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def recognize_speech():
    """Captures microphone input and converts speech to text."""
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=10)  # Listen with a timeout
            text = recognizer.recognize_google(audio)  # Use Google's API
            print(f"🗣 Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("❌ Error with recognition service.")
            return ""
        except sr.WaitTimeoutError:
            print("⏳ No speech detected, try again.")
            return ""

if __name__ == "__main__":
    recognize_speech()

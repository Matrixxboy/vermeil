import speech_recognition as sr
import time

# Initialize recognizer
recognizer = sr.Recognizer()

def recognize_speech(duration=600):  # 600 seconds = 10 minutes
    """Continuously listens for speech input for a set duration."""
    with sr.Microphone() as source:
        print(f"🎤 Listening for commands for {duration // 60} minutes...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        
        start_time = time.time()  # Track start time
        while (time.time() - start_time) < duration:
            try:
                print("🎙 Speak now...")
                audio = recognizer.listen(source, timeout=10)  # Timeout to prevent infinite wait
                text = recognizer.recognize_google(audio)  # Convert speech to text
                
                if text:
                    print(f"🗣 Recognized: {text}")
                    return text.lower()  # Return recognized command

            except sr.WaitTimeoutError:
                print("⏳ No speech detected. Waiting for input...")
                continue  # Keep waiting if no speech detected
            except sr.UnknownValueError:
                print("❌ Sorry, I couldn't understand.")
                continue  # Keep listening
            except sr.RequestError:
                print("❌ Error with recognition service.")
                return None  # Return None if there's an issue with recognition

    print("💤 No command detected for 10 minutes. Going back to sleep...")
    return None  # Return None to signal timeout and go back to wake-word mode

if __name__ == "__main__":
    recognize_speech()

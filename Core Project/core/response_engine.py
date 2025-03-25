import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech and speak it aloud."""
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak()

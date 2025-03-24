import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech and speak it aloud."""
    engine.say(text)
    engine.runAndWait()

def respond(intent):
    """Generate response based on intent and speak it."""
    responses = {
        "time": "The current time is {time.strftime('%I:%M %p')}",  # Placeholder time
        "shutdown": "Shutting down Vermeil AI. Goodbye!",
        "unknown": "I'm sorry, I didn't understand that."
    }

    response = responses.get(intent, "I'm not sure how to respond to that.")
    print(response)  # Print response
    speak(response)  # Speak response

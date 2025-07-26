import spacy
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech and speak it aloud."""
    engine.say(text)
    engine.runAndWait()

# Try loading the model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("❌ spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm")
    exit(1)

# Define intent keywords
INTENTS = {
    "open_app": ["open", "launch", "start"],
    "weather": ["weather", "forecast", "temperature"],
    "time": ["time", "clock", "hour"],
    "shutdown": ["shutdown", "turn off", "power off"]
}

def recognize_intent(user_input):
    """Recognizes intent based on predefined keywords."""
    if not user_input.strip():
        return "unknown"

    doc = nlp(user_input.lower())  # Process text with spaCy NLP
    for intent, keywords in INTENTS.items():
        if any(token.text in keywords for token in doc):
            return intent  # Return detected intent
    return "unknown"

def process_command(command):
    """Processes the recognized intent and executes appropriate action."""
    intent = recognize_intent(command)
    # print(f"🎯 Recognized Intent: {intent}") #it will shows the command in terminal

    if intent == "time":
        print(f"Current time is {time.strftime('%I:%M %p')}")  # Dynamic current time
        speak(f"Current time is {time.strftime('%I:%M %p')}")  # Dynamic current time

    elif intent == "shutdown":
        speak("🛑 Shutting down Vermeil AI...")
        return True  # Return True to signal AI shutdown

    return False  # Return False to keep AI running

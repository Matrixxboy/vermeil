import spacy
import json
import os
from memory import INTENTS
from response_engine import speak
from speech_recog import recognize_speech

try:
    nlp = spacy.load("en_core_web_md")  # Use "en_core_web_md" for better accuracy
except OSError:
    print("❌ Model not found! Run: python -m spacy download en_core_web_md")
    exit(1)

# Load memory file
MEMORY_FILE = os.path.join(os.path.dirname(__file__), "../config/memory.json")

# Load existing commands
def load_memory():
    """Load saved commands from memory.json."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}  # Return empty dict if file doesn't exist

# Save new commands
def save_memory(data):
    """Save new commands to memory.json."""
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load memory data
MEMORY_DATA = load_memory()

def recognize_intent(user_input):
    """Recognizes intent using NLP similarity scoring."""
    if not user_input.strip():
        return "unknown"

    doc = nlp(user_input.lower())  # Process text


    # ✅ Check INTENTS and their samples
    for intent, data in INTENTS.items():
        for sample in data["samples"]:
            # print(f"🔍 Checking intent '{intent}' with sample '{sample}'")
            if user_input.lower() == sample:
                print(f"✅ Matched Intent: {intent}")
                return intent

    # Check in learned commands
    if user_input.lower() in MEMORY_DATA:
        print("✅ Found in learned commands")
        return "learned"

    print("❌ No match found, returning unknown")
    return "unknown"

def process_command(command):
    """Processes the recognized intent and executes appropriate action."""
    intent = recognize_intent(command)

    if intent in INTENTS:
        response = INTENTS[intent].get("response", "I don’t have a response for this.")

        print(f"🤖 {response}")  # Print response to terminal
        speak(response)  # Speak response

        if intent == "shutdown":
            return "shutdown"  # Exit the program

    elif intent == "learned":
        response = MEMORY_DATA.get(command.lower(), "Sorry, I forgot this command.")
        print(f"🤖 {response}")
        speak(response)

    else:
        # Unrecognized command - ask to learn
        print("🤖 I don’t know this command. Would you like to teach me? (yes/no)")
        speak("I don’t know this command. Would you like to teach me?")
        user_response = input("User: ").strip().lower()

        if user_response == "yes":
            print("🔹 What should I reply when you say this?")
            speak("What should I reply when you say this?")
            new_response = input("User: ").strip()

            MEMORY_DATA[command.lower()] = new_response
            save_memory(MEMORY_DATA)

            print("✅ Got it! I'll remember this command.")
            speak("Got it! I'll remember this command.")

    return "continue"  # Continue listening for more commands

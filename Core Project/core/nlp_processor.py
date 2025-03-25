import spacy
import time
from memory import INTENTS
from response_engine import speak

try:
    nlp = spacy.load("en_core_web_md")  # Use "en_core_web_md" for better accuracy
except OSError:
    print("❌ Model not found! Run: python -m spacy download en_core_web_md")
    exit(1)

def recognize_intent(user_input):
    """Recognizes intent using NLP similarity scoring."""
    if not user_input.strip():
        return "unknown"

    doc = nlp(user_input.lower())  # Process text
    best_match = None
    best_score = 0.0

    for intent, data in INTENTS.items():
        for sample in data["samples"]:
            sample_doc = nlp(sample)  # Process stored samples
            similarity = doc.similarity(sample_doc)  # Compare similarity
            
            if similarity > best_score:
                best_score = similarity
                best_match = intent

    return best_match if best_score > 0.6 else "unknown"  # Set 60% similarity threshold

def process_command(command):
    """Processes the recognized intent and executes appropriate action."""
    intent = recognize_intent(command)

    if intent in INTENTS:
        response = INTENTS[intent]["response"]

        # Replace {time} placeholder dynamically
        if "{time}" in response:
            response = response.replace("{time}", time.strftime("%I:%M %p"))

        print(response)  # Print response to terminal
        speak(response)  # Speak response

        if intent == "shutdown":
            return True  # Return True to signal AI shutdown

    return False  # Return False to keep AI running

import spacy

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

# Example usage
if __name__ == "__main__":
    while True:
        command = input("You: ").strip()
        if not command:
            continue  # Ignore empty input

        intent = recognize_intent(command)
        print(f"Recognized Intent: {intent}")

        if intent == "time":
            print("Current time: 12:30 PM")  # Placeholder time
        elif intent == "shutdown":
            print("Shutting down Vermeil AI...")
            break

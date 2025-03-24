import sys
import os

# Get the absolute path of the core directory
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Core Project/core"))

# Add core directory to Python's module search path
sys.path.append(CORE_DIR)

# Now, import wake word and speech recognition
from wake_word import listen_for_wake_word
from speech_recog import recognize_speech
from nlp_processor import recognize_intent

while True:
    text = recognize_speech()
    if listen_for_wake_word():  # Wake word detection
        print("✅ Wake word detected! Starting speech recognition...")
        command = recognize_speech()
        print(f"🗣 Command: {command}")
            
        if text:
            intent = recognize_intent(text)
            print(f"Recognized Intent: {intent}")
            



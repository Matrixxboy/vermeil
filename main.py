import sys
import os

# Get the absolute path of the core directory
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Core Project/core"))

# Add core directory to Python's module search path
sys.path.append(CORE_DIR)
from wake_word import listen_for_wake_word
from speech_recog import recognize_speech
from nlp_processor import process_command

while True:
    if listen_for_wake_word():  # Wake word detection
        print("✅ Wake word detected! Starting speech recognition...")
        command = recognize_speech()
        print(f"🗣 Command: {command}")

        if command:
            should_exit = process_command(command)
            if should_exit:
                break  # Exit the loop when "shutdown" is detected

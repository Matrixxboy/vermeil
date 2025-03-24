import sys
import os
import time

# Get the absolute path of the core directory
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Core Project/core"))

# Add core directory to Python's module search path
sys.path.append(CORE_DIR)

# Import wake word, speech recognition, and NLP processor
from wake_word import listen_for_wake_word
from speech_recog import recognize_speech
from nlp_processor import process_command  # Instead of recognize_intent

# Set sleep time (in minutes)
SLEEP_TIME = 5  # AI will sleep after 5 minutes of inactivity

# Track last activity time
last_activity_time = time.time()

while True:
    # Check if AI has been inactive for too long
    if time.time() - last_activity_time > SLEEP_TIME * 60:
        print("😴 Vermeil AI is going to sleep due to inactivity...")
        break

    if listen_for_wake_word():  # Wake word detection
        last_activity_time = time.time()  # Reset inactivity timer
        print("✅ Wake word detected! Starting speech recognition...")
        
        command = recognize_speech()
        if command:
            print(f"🗣 Command: {command}")
            
            # Send command to nlp_processor for processing
            if process_command(command):  
                break  # If shutdown command is received, stop AI

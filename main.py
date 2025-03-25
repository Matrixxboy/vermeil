import sys
import os
import time

# Get the absolute path of the core directory
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Core Project/core"))

# Add core directory to Python's module search path
sys.path.append(CORE_DIR)

from wake_word import listen_for_wake_word
from speech_recog import recognize_speech
from nlp_processor import process_command
from response_engine import speak

ACTIVE_DURATION = 600  # 10 minutes in seconds

while True:
    if listen_for_wake_word():  # Wake word detection
        print("✅ Wake word detected! Vermeil is listening...")
        speak("I am listening!")

        start_time = time.time()  # Record start time
        while (time.time() - start_time) < ACTIVE_DURATION:
            command = recognize_speech()
            print(f"🗣 Command: {command}")

            if command:
                result = process_command(command)

                if result == "shutdown":
                    listen_for_wake_word()

        print("⏳ 10 minutes passed. Going to sleep...")
        speak("Time's up! I will wait for your command again.")

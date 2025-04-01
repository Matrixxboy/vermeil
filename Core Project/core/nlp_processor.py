import spacy
import json
import os
import logging
import traceback
from datetime import datetime
from memory import INTENTS
from response_engine import speak
from speech_recog import recognize_speech

# Configure logging for normal logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Error log file
ERROR_LOG_FILE = os.path.join(os.path.dirname(__file__), "../../logs/error.log")

def log_error(exception):
    """Logs errors with time, file name, and line number into error.json"""
    error_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "error": str(exception),
        "file": traceback.extract_tb(exception.__traceback__)[-1].filename,
        "line": traceback.extract_tb(exception.__traceback__)[-1].lineno,
        "function": traceback.extract_tb(exception.__traceback__)[-1].name
    }
    try:
        if os.path.exists(ERROR_LOG_FILE):
            with open(ERROR_LOG_FILE, "r", encoding="utf-8") as file:
                error_logs = json.load(file)
        else:
            error_logs = []
        error_logs.append(error_info)
        with open(ERROR_LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(error_logs, file, indent=4)
        logging.error(f"❌ Error logged: {error_info}")
    except Exception as e:
        logging.error(f"❌ Failed to write to error.json: {e}")

try:
    nlp = spacy.load("en_core_web_md")
except OSError as e:
    log_error(e)
    logging.error("❌ Model not found! Run: python -m spacy download en_core_web_md")
    exit(1)

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "../config/memory.json")

def load_memory():
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
    except json.JSONDecodeError as e:
        log_error(e)
        logging.warning("⚠️ Corrupted memory.json file! Resetting...")
        return {}
    return {}

def save_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        log_error(e)
        logging.error(f"❌ Failed to save memory: {e}")

MEMORY_DATA = load_memory()

def recognize_intent(user_input):
    try:
        if not user_input.strip():
            return "unknown"
        doc = nlp(user_input.lower())
        for intent, data in INTENTS.items():
            for sample in data["samples"]:
                if user_input.lower() == sample:
                    logging.info(f"✅ Matched Intent: {intent}")
                    return intent
        if user_input.lower() in MEMORY_DATA:
            logging.info("✅ Found in learned commands")
            return "learned"
        logging.warning("❌ No intent matched. Returning 'unknown'.")
        return "unknown"
    except Exception as e:
        log_error(e)
        return "unknown"

def process_intent(matched_intent):
    """Handles intent processing."""
    response = INTENTS[matched_intent]["response"]
    if callable(response):  # ✅ Check if it's a function before calling
        response = response()
    return response

def process_command(command):
    try:
        intent = recognize_intent(command)
        if intent in INTENTS:
            response = process_intent(intent)  # ✅ Now calling process_intent
            logging.info(f"🤖 Responding: {response}")
            speak(response)
            if intent == "shutdown":
                return "shutdown"
        elif intent == "learned":
            response = MEMORY_DATA.get(command.lower(), "Sorry, I forgot this command.")
            logging.info(f"🤖 Learned Response: {response}")
            speak(response)
        else:
            logging.info("🤖 Unrecognized command. Asking to learn.")
            speak("I don’t know this command. Would you like to teach me?")
            user_response = input("User: ").strip().lower()
            if user_response == "yes":
                speak("What should I reply when you say this?")
                new_response = input("User: ").strip()
                MEMORY_DATA[command.lower()] = new_response
                save_memory(MEMORY_DATA)
                logging.info("✅ Learned new command.")
                speak("Got it! I'll remember this command.")
        return "continue"
    except Exception as e:
        log_error(e)
        return "continue"

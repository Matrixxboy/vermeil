import sys
import os
import time
import textwrap
from core_project.MCP.mcp import collect_contexts

# Get the absolute path of the core directory
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "core_project/core"))

# Add core directory to Python's module search path
sys.path.append(CORE_DIR)
from speech_recog import listen
from wake_word import listen_for_wake_word
from Model_client import query_llm
from response_engine import speak
# Import wake word, speech recognition, and NLP processor

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
        while True:
            try:
                user_input = listen()
                print(f"🧑 You: {user_input}")

                if user_input.lower() in ["exit", "quit"]:
                    print("👋 Goodbye.")
                    break

                context = collect_contexts()
                full_prompt = f"[System Info]\n{context}\n\n[User]: {user_input}\n[Assistant]:"
                print("📡 Sending to LLM...")

                response = query_llm(full_prompt)
                print("\n🤖 Vermeil:\n", textwrap.fill(response, 80))
                speak(response)

            except Exception as e:
                print("⚠️ Error:", e)


import sys
import os
import time
import textwrap

# 🧠 Set core path and import from it
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "core_project/core"))
sys.path.append(CORE_DIR)

from speech_recog import listen
from Model_client import query_llm
from response_engine import speak
from core_project.MCP.mcp import collect_contexts

# Sleep configuration (minutes)
SLEEP_TIME = 5
last_activity_time = time.time()

print("💡 Vermeil AI is now running. Say something...")

while True:
    if time.time() - last_activity_time > SLEEP_TIME * 60:
        print("😴 Vermeil AI is going to sleep due to inactivity...")
        break

    try:
        user_input = listen()

        # Check if speech was detected
        if user_input is None:
            print("⚠ No input detected, please try again.")
            continue  # go back to listening

        # Now safe to strip and lowercase
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye.")
            break

        # Otherwise, process the input
        print(f"💬 You said: {user_input}")



        # Detect context needs from user input
        selected_mcp = []
        lowered_input = user_input.lower()
        if "weather" in lowered_input:
            selected_mcp.append("weather")
        if "time" in lowered_input or "date" in lowered_input:
            selected_mcp.append("time")
        if "system" in lowered_input or "cpu" in lowered_input:
            selected_mcp.append("system")
        if "location" in lowered_input or "where" in lowered_input:
            selected_mcp.append("location")

        # Default MCP if none matched
        if not selected_mcp:
            selected_mcp = ["time"]

        # Collect contextual information
        context = collect_contexts(selected_mcp)
        full_prompt = f"[System Info]\n{context}\n\n[User]: {user_input}\n[Assistant]:"

        print("📡 Sending to LLM...")
        response = query_llm(full_prompt)

        print("\n🤖 Vermeil:\n", textwrap.fill(response, 80))
        speak(response)

        last_activity_time = time.time()  # Reset sleep timer

    except Exception as e:
        print("⚠️ Error:", e)

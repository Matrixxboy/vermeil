import time
from datetime import date

from plugins.weather import get_weather
from plugins.jokes import tell_joke
from plugins.math_engine import solve_math_expression
from plugins.vision import start_vision_mode, scan_current_frame, close_vision_mode

INTENTS = {
    # Greetings
    "greeting": {
        "samples": ["hello", "hi", "hey", "good morning", "good evening", "what's up"],
        "response": "Hello! How can I assist you today?"
    },
    
    # Time-related queries
    "time": {
        "samples": ["what time is it", "what time it is","current time", "tell me the time"],
        "response": "The time is "+time.strftime("%I:%M %p")+" ."
    },
    
    # Date-related queries
    "date": {
        "samples": ["what's today's date", "current date", "what day is it today","today's date"],
        "response": "Today's date is "+date.today().strftime("%A, %B %d, %Y")+"."
    },

    # System Shutdown / Sleep Mode
    "shutdown": {
        "samples": ["shutdown","shut down", "turn off", "go to sleep","sleep mode","sleepmode"],
        "response": "Okay, I will wait for you to wake me up."
    },

    # Weather-related queries
    "weather": {
        "samples": ["what's the weather like", "current weather", "is it raining", "is it sunny today"],
        "response": get_weather
    },

    # General Knowledge
    "who_are_you": {
        "samples": ["who are you", "what is your name", "introduce yourself"],
        "response": "I am Vermeil, your personal AI assistant."
    },
    
    "how_are_you": {
        "samples": ["how are you", "how's it going", "how do you feel"],
        "response": "I'm just a program, but I'm feeling quite functional today!"
    },

    # Fun responses (Jokes, Quotes)
    "joke": {
        "samples": ["tell me a joke", "make me laugh", "funny joke"],
        "response": tell_joke
    },

    "quote": {
        "samples": ["give me a quote", "inspire me", "motivation"],
        "response": "The only way to do great work is to love what you do. - Steve Jobs"
    },

    # Basic Math
    "mathematics": {
        "samples": ["i need help in math","maths problem"],
        "response": solve_math_expression
    },

    # System Commands
    "restart": {
        "samples": ["restart", "reboot"],
        "response": "Restarting now... Just kidding! I can't actually restart anything."
    },
    
    "battery_status": {
        "samples": ["what's my battery", "battery status", "battery percentage"],
        "response": "I can't check your battery directly, but you can check your system settings."
    },

    # Opening Applications (Customizable)
    "open_browser": {
        "samples": ["open browser", "start chrome", "launch firefox"],
        "response": "I can't open apps yet, but you can launch it manually!"
    },

    # Personalization
    "favorite_color": {
        "samples": ["what's your favorite color","what's your favorite colour", "do you like colors","do you like colorus"],
        "response": "I like all colors, but purple is quite nice!"
    },

    # Random Facts
    "fact": {
        "samples": ["tell me a fact", "give me a random fact", "random knowledge"],
        "response": "Did you know? A group of flamingos is called a 'flamboyance'!"
    },

    # Closing Chat
    "goodbye": {
        "samples": ["goodbye", "bye", "see you later"],
        "response": "Goodbye! Have a great day!"
    },
    
    # the computer vision command 
    "start_vision": {
        "samples": ["start scanning", "start vision mode", "activate camera"],
        "response": start_vision_mode
    },

    "scan_now": {
        "samples": ["scan this", "what is this", "analyze this"],
        "response": scan_current_frame
    },

    "close_vision": {
        "samples": ["close vision", "stop scanning", "deactivate camera"],
        "response": close_vision_mode
    },

}

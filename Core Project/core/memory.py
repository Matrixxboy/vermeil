# Dictionary storing intents and sample queries
INTENTS = {
    "open_app": {
        "samples": ["open", "launch", "start", "run"],
        "response": "Opening the application."
    },
    "weather": {
        "samples": ["weather", "forecast", "temperature", "tell me the weather", "what's the weather like"],
        "response": "Checking the weather for you."
    },
    "time": {
        "samples": ["time", "clock", "what time is it", "current time"],
        "response": "Current time is {time}."
    },
    "shutdown": {
        "samples": ["shutdown", "turn off", "power off", "exit AI", "close AI"],
        "response": "Shutting down Vermeil AI."
    }
}

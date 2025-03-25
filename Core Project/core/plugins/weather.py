import requests
import json
import os
import datetime
from dotenv import load_dotenv



def get_weather():
    """Fetches live weather data from Open-Meteo API."""
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=21.1959&longitude=72.8302&hourly=temperature_2m")
        weather_data = response.json()

        # Extract current hour's temperature
        current_hour = datetime.datetime.utcnow().hour
        temperature = weather_data["hourly"]["temperature_2m"][current_hour]

        return f"The current temperature is {temperature}°C in Surat."

    except Exception as e:
        return "Sorry, I couldn't fetch the weather. Please try again later."

# Test function
if __name__ == "__main__":
    print(get_weather())
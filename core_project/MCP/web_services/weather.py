import requests
import geocoder

def get_weather_context():
    try:
        g = geocoder.ip('me')
        lat, lon = g.latlng
        weather_api = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        res = requests.get(weather_api).json()
        temp = res["current_weather"]["temperature"]
        wind = res["current_weather"]["windspeed"]
        return f"Weather: {temp}°C, Wind: {wind} km/h"
    except Exception:
        return "Weather: unavailable"

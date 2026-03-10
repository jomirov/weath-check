from flask import request
import json
from modules import apiQuery

def weather():
    city = request.args.get("city")
    data = apiQuery.checkWeather(city, "weather")

    current_weather = {
        "primary": {
            "city": data["name"],
            "weather": data["weather"][0]["main"],
            "temp": data["main"]["temp"]
        },
        "secondary": {
            "feels_like": data["main"]["feels_like"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "wind_direction": data["wind"]["deg"],
            "cloudiness": data["clouds"]["all"]
        }
    }

    with open("json/weather.json", "w", encoding="utf-8") as file:
        json.dump(current_weather, file, ensure_ascii=False, indent=4)
    
    with open("json/weather.json", "r", encoding="utf-8") as file:
        return json.load(file)
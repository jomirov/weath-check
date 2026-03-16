import requests
import os
from dotenv import load_dotenv
from api_clients.ipAPI import getCity

load_dotenv()

api_key_weather = os.getenv("API_KEY_WEATHER")

def checkWeather(city, check_type): #checktype - weather/forecast
    if city == None:
        city = getCity()

    api_url = f"https://api.openweathermap.org/data/2.5/{check_type}?q={city}&appid={api_key_weather}&units=metric&lang=ru"

    if requests.get(api_url).status_code == 404:
        print(requests.get(api_url).status_code)
        city = getCity()

    api_url = f"https://api.openweathermap.org/data/2.5/{check_type}?q={city}&appid={api_key_weather}&units=metric&lang=ru"

    return requests.get(api_url).json()
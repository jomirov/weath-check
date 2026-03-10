import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def checkWeather(city, check_type): #checktype - weather/forecast
    api_url = f"https://api.openweathermap.org/data/2.5/{check_type}?q={city}&appid={api_key}&units=metric&lang=ru"

    return requests.get(api_url).json()
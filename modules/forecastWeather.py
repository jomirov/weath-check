from flask import request
from modules import apiQuery
import json
from datetime import datetime, timedelta

def weather():
    city = request.args.get("city")
    data = apiQuery.checkWeather(city, "forecast")
    
    now = datetime.now()


    forecast_for_one_day = []
    fifteen_hours = now + timedelta(hours=15)

    for record in data["list"]:
        if len(forecast_for_one_day) != 6 and datetime.fromtimestamp(record["dt"]) < fifteen_hours:
            forecast_for_one_day.append(
                {
                    "time": record["dt_txt"],
                    "weather_type": record["weather"][0]["main"],
                    "temp": record["main"]["temp"]
                }
            )


    forecast_for_five_days = []
    five_days = now + timedelta(days=5)
    group_dates = []

    for record in data["list"]:
        converted_date = datetime.strptime(record["dt_txt"].split()[0], "%Y-%m-%d")
        if len(forecast_for_five_days) != 6 and converted_date < five_days:
            if converted_date not in group_dates:
                group_dates.append(converted_date)
                forecast_for_five_days.append(
                    {
                        "time": str(converted_date).split()[0],
                        "weather_type": record["weather"][0]["main"],
                        "temp": record["main"]["temp"]
                    }
                )
    

    with open("json/forecast.json", "w", encoding="utf-8") as file:
        json.dump({"forecast_for_one_day": forecast_for_one_day, "forecast_for_five_days": forecast_for_five_days}, file, ensure_ascii=False, indent=4)

    with open("json/forecast.json", "r") as file:
        return json.load(file)
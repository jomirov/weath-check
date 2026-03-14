import api_clients.weatherAPI as weatherAPI
from datetime import timedelta, datetime


class Weather:
    def __init__(self, city):
        self.city = city

class CurrentWeather(Weather):
    def getCurrent(self):
        data = weatherAPI.checkWeather(self.city, "weather")

        current_weather_data = {
            "primary": {
                "city": data["name"],
                "weather": data["weather"][0]["main"],
                "temp": round(data["main"]["temp"])
            },
            "secondary": {
                "feels_like": round(data["main"]["feels_like"]),
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "wind_direction": data["wind"]["deg"],
                "cloudiness": data["clouds"]["all"]
            }
        }

        return current_weather_data



class ForecastWeather(Weather):
    def getForecast(self):
        data = weatherAPI.checkWeather(self.city, "forecast")
        
        now = datetime.now()

        forecast_for_one_day = []
        fifteen_hours = now + timedelta(hours=15)


        forecast_for_five_days = []
        five_days = now + timedelta(days=5)
        group_dates = []

        for record in data["list"]:
            if len(forecast_for_one_day) != 6 and datetime.fromtimestamp(record["dt"]) < fifteen_hours:
                forecast_for_one_day.append( 
                    {
                        "time": record["dt_txt"],
                        "weather_type": record["weather"][0]["main"],
                        "temp": round(record["main"]["temp"])
                    }
                )

            converted_date = datetime.strptime(record["dt_txt"].split()[0], "%Y-%m-%d")
            if len(forecast_for_five_days) != 6 and converted_date < five_days:
                if converted_date not in group_dates:
                    group_dates.append(converted_date)
                    forecast_for_five_days.append(
                        {
                            "time": str(converted_date).split()[0],
                            "weather_type": record["weather"][0]["main"],
                            "temp": round(record["main"]["temp"])
                        }
                    )
        
        return {"forecast_for_one_day": forecast_for_one_day, 
                "forecast_for_five_days": forecast_for_five_days}
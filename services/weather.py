import api_clients.weatherAPI as weatherAPI
from datetime import timedelta, datetime
from services import weather_details_setter, wind_direction_checker

class Weather:
    def __init__(self, city):
        self.city = city

class CurrentWeather(Weather):
    def getCurrent(self):
        data = weatherAPI.checkWeather(self.city, "weather")

        f_data = weatherAPI.checkWeather(self.city, "forecast")
        night_temp = 0
        for record in f_data["list"][:8]:
            if record["dt_txt"].split()[1] == "00:00:00":
                night_temp = record["main"]["temp"]

        date_str = str(datetime.fromtimestamp(data["dt"])).split()[0][-4:]
        date = datetime.strptime(date_str, "%m-%d")
        days = ["Чт", "Пт", "Сб", "Вс", "Пн", "Вт", "Ср"]
        months = ["января", "февраля", "марта", "апреля", "мая", "июня", 
        "июля", "августа", "сентября", "ноября", "октября"]
        named_date = f"{days[date.weekday()]}. {date.day} {months[date.month-1]}"

        weather_type = data["weather"][0]["main"]
        weather_icon = weather_details_setter.iconSet(weather_type)
        weather_background = weather_details_setter.backgroundSet(weather_type)

        wind_direction = wind_direction_checker.checkDirection(data["wind"]["deg"])

        sunrise = str(datetime.fromtimestamp(data["sys"]["sunrise"])).split()[1][-8:][:-3]
        sunset = str(datetime.fromtimestamp(data["sys"]["sunset"])).split()[1][-8:][:-3]

        current_weather_data = {
            "primary": {
                "city": data["name"],
                "weather": data["weather"][0]["main"],
                "temp": round(data["main"]["temp"]),
                "night_temp": round(night_temp),
                "date": named_date,
                "weather_icon": weather_icon,
                "weather_background": weather_background
            },
            "secondary": {
                "feels_like": round(data["main"]["feels_like"]),
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "wind_direction": wind_direction,
                "cloudiness": data["clouds"]["all"],
                "sunrise": sunrise,
                "sunset": sunset
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
                weather_icon = weather_details_setter.iconSet(record["weather"][0]["main"])
                forecast_for_one_day.append( 
                    {
                        "time": record["dt_txt"][-8:][:5],
                        "weather_type": record["weather"][0]["main"],
                        "temp": round(record["main"]["temp"]),
                        "weather_icon": weather_icon
                    }
                )

            converted_date = datetime.strptime(record["dt_txt"].split()[0], "%Y-%m-%d")
            if len(forecast_for_five_days) != 6 and converted_date < five_days:
                if converted_date not in group_dates:
                    weather_icon = weather_details_setter.iconSet(record["weather"][0]["main"])
                    group_dates.append(converted_date)
                    forecast_for_five_days.append(
                        {
                            "time": str(converted_date).split()[0][5:],
                            "weather_type": record["weather"][0]["main"],
                            "temp": round(record["main"]["temp"]),
                            "weather_icon": weather_icon
                        }
                    )
        
        return {"forecast_for_one_day": forecast_for_one_day, 
                "forecast_for_five_days": forecast_for_five_days}
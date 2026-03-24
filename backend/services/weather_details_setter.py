def iconSet(weather_type):
    weather_icon = ""
    if weather_type == "Mist" or weather_type == "Clouds" or weather_type == "Fog":
        weather_icon = "cloudy_icon.png"
    elif weather_type == "Clear":
        weather_icon = "sunny_icon.png"
    elif weather_type == "Rain" or weather_type == "Thunderstorm":
        weather_icon = "rainy_icon.png"
    elif weather_type == "Snow":
        weather_icon = "snowy_icon.png"
    return weather_icon

def backgroundSet(weather_type):
    weather_background = ""
    if weather_type == "Mist" or weather_type == "Clouds" or weather_type == "Fog":
        weather_background = "cloudy_background.png"
    elif weather_type == "Clear":
        weather_background = "sunny_background.png"
    elif weather_type == "Rain" or weather_type == "Thunderstorm":
        weather_background = "rainy_background.png"
    elif weather_type == "Snow":
        weather_background = "snowy_background.png"
    return weather_background
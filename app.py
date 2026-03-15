from flask import Flask, request, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from services import weather

app = Flask(__name__)

app.config["CACHE_TYPE"] = "SimpleCache"

cache = Cache()

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per minute"],
    storage_uri="memory://",
)

@cache.cached(timeout=300)
@app.route('/')
def home():
    city = request.args.get("city")
    current_weather_data = weather.CurrentWeather(city).getCurrent()
    forecast_weather_data = weather.ForecastWeather(city).getForecast()
    return render_template("index.html", 
                           current_weather_data=current_weather_data, 
                           forecast_weather_data=forecast_weather_data)

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route("/ratetest")
@limiter.limit("10 per minute")
def ratetest():
    return 0

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
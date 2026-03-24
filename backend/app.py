from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from services import weather
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config["CACHE_TYPE"] = "SimpleCache"

cache = Cache(app=app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per minute"],
    storage_uri="memory://",
)

@app.route('/')
@cache.cached(timeout=300)
def home():
    city = request.args.get("city")
    current_weather_data = weather.CurrentWeather(city).getCurrent()
    forecast_weather_data = weather.ForecastWeather(city).getForecast()
    return jsonify(
        {
            "current_weather_data": current_weather_data,
            "forecast_weather_data": forecast_weather_data
        }
    )

@app.route("/ratetest")
@limiter.limit("10 per minute")
def ratetest():
    return 0

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
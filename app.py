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

@app.route('/')
def home():
    return render_template("index.html")

@cache.cached(timeout=300)
@app.route('/data-weather')
def getCurrentWeather():
    city = request.args.get("city")
    return weather.CurrentWeather(city).getCurrent()

@cache.cached(timeout=300)
@app.route("/data-forecast")
def getForecastWeather():
    city = request.args.get("city")
    return weather.ForecastWeather(city).getForecast()

@app.route("/ratetest")
@limiter.limit("10 per minute")
def ratetest():
    return 0

if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")
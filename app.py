from flask import Flask, render_template
from modules import currentWeather, forecastWeather
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per minute"],
    storage_uri="memory://",
)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data-weather')
def getCurrentWeather():
    return currentWeather.weather()

@app.route("/data-forecast")
def getForecastWeather():
    return forecastWeather.weather()

@app.route("/ratetest")
@limiter.limit("10 per minute")
def ratetest():
    return 0

if __name__ == "__main__":
    app.run(debug=True)
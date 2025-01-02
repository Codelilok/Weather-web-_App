from flask import Flask, render_template, request
import requests
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        units = request.form["units"]

        api_key = "cd95bfc489f09469cb862762755b86bd"
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"

        try:
            # Fetch current weather data
            weather_response = requests.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

            # Fetch forecast data
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
        except requests.exceptions.RequestException as e:
            error = f"Error fetching data: {e}"

    return render_template(
        "index.html", 
        weather_data=weather_data, 
        forecast_data=forecast_data, 
        error=error, 
        units=request.form.get("units", "metric")
    )

@app.template_filter("datetime")
def format_datetime(value):
    return datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S")

# Comment or remove the following line, as Gunicorn will handle the app execution
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host="0.0.0.0", port=port)
import requests
from django_cron import CronJobBase, Schedule
from .models import WeatherData
from datetime import date, datetime

WEATHER_API_KEY = "e4072f7bfe094aee9a4175410252901"

class FetchWeatherCronJob(CronJobBase):
    RUN_AT_TIMES = ["00:00"]  # Runs at midnight
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "weather.fetch_weather_cron"

    def do(self):
        countries = ["Uzbekistan", "Russia", "USA", "India", "Germany", "France"]  # Extend this list
        today = date.today()

        for country in countries:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={country}&days=1&aqi=no&alerts=no"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                location = data["location"]
                forecast = data["forecast"]["forecastday"][0]["hour"]  # Get hourly forecast

                temp_c = {}
                wind_kph = {}
                cloud = {}

                for hour in forecast:
                    hour_time = datetime.strptime(hour["time"], "%Y-%m-%d %H:%M").strftime("%H:%M")
                    temp_c[hour_time] = hour["temp_c"]
                    wind_kph[hour_time] = hour["wind_kph"]
                    cloud[hour_time] = hour["cloud"]

                # Store the data in the database
                WeatherData.objects.update_or_create(
                    country=location["country"],
                    city=location["name"],
                    date_recorded=today,
                    defaults={
                        "lat": location["lat"],
                        "lon": location["lon"],
                        "temp_c": temp_c,
                        "wind_kph": wind_kph,
                        "cloud": cloud,
                    }
                )
                print(f"Weather data updated for {country}")

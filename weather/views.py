from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import WeatherData
from .utils import get_temp_color, get_wind_color, get_cloud_color
from datetime import date, datetime

class GetWeather(APIView):
    permission_classes = [IsAuthenticated]  # Requires authentication

    def get(self, request):
        country_names = request.GET.getlist("country")
        current_time = datetime.now().strftime("%H:%M")  # Get current time in "HH:MM" format

        if not country_names:
            return Response({"error": "At least one country name is required"}, status=400)

        today = date.today()
        weather_entries = WeatherData.objects.filter(country__in=country_names, date_recorded=today)

        if not weather_entries.exists():
            return Response({"error": "No weather data found for the given countries"}, status=404)

        results = []
        for entry in weather_entries:
            # Find the closest hour
            available_hours = list(entry.temp_c.keys())
            closest_hour = min(available_hours, key=lambda h: abs(datetime.strptime(h, "%H:%M") - datetime.strptime(current_time, "%H:%M")))

            results.append({
                "name": entry.city,
                "country": entry.country,
                "lat": entry.lat,
                "lon": entry.lon,
                "temp_c": entry.temp_c[closest_hour],
                "temp_color": get_temp_color(entry.temp_c[closest_hour]),
                "wind_kph": entry.wind_kph[closest_hour],
                "wind_color": get_wind_color(entry.wind_kph[closest_hour]),
                "cloud": entry.cloud[closest_hour],
                "cloud_color": get_cloud_color(entry.cloud[closest_hour]),
            })

        return Response(results)
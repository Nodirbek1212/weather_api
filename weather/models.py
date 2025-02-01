from django.db import models

class WeatherData(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

    temp_c = models.JSONField()  # Stores hourly temperature as JSON
    wind_kph = models.JSONField()  # Stores hourly wind speed as JSON
    cloud = models.JSONField()  # Stores hourly cloud coverage as JSON

    def __str__(self):
        return f"{self.city}, {self.country} - {self.date_recorded}"

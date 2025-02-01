from django.urls import path
from .views import GetWeather

urlpatterns = [
    path("get-weather/", GetWeather.as_view(), name="get_weather"),
]

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
import requests

# Create your models here.
class City(models.Model):
    CITIES = [
              ('Prague', 'Praha'),
              ('Brno', 'Brno'),
              ('Liberec', 'Liberec'),
              ('Ostrava', 'Ostrava'),
              ('České Budějovice', 'České Budějovice'),
              ('Karlovy Vary', 'Karlovy Vary'),
              ('Litoměřice', 'Litoměřice'),
             ]

    # just one model in db
    cityName = models.CharField(max_length=30, verbose_name=('City Name'), choices=CITIES)

    api_address = "http://api.openweathermap.org/data/2.5/weather?q=Prague&appid=fb7aed4ba4c5be80800a55852257ca28"

    json_data = requests.get(api_address).json()
    kelvin = json_data["main"]["temp"]
    celsius = round(kelvin - 273.15, 2)

    for item in json_data['weather']:
        get_weather_type = item['main']

    for item in json_data['weather']:
        get_weather_desc = item['description']

    currentTemp = celsius
    weatherType = get_weather_type
    weatherDesc = get_weather_desc
    windSpeed = json_data["wind"]["speed"]
    currentTime = datetime.now()
    # time only updates when starting server - fix that

    # get city url by id for use in templates
    def getCityUrl(self):
        return reverse('city_detail_view', kwargs={'id': self.id})


    def __str__(self):
        return self.cityName

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
              ('Cheb', 'Cheb'),
              ('Mladá Boleslav', 'Mladá Boleslav'),
              ('Olomouc', 'Olomouc'),
              ('Hradec Králové', 'Hradec Králové'),
              ('Plzeň', 'Plzeň'),
              ('Doksy', 'Doksy'),
              ('Roudnice nad Labem', 'Roudnice nad Labem'),
              ('Ústí nad Labem', 'Ústí nad Labem'),
              ('Děčín', 'Děčín'),
              ('Snědovice', 'Snědovice'),
              ('London', 'London'),
              ('Oxford', 'Oxford'),
              ('Liverpool', 'Liverpool'),
              ('Glasgow', 'Glasgow'),
              ('Dublin', 'Dublin'),
              ('Berlin', 'Berlin'),
              ('Munchen', 'Munchen'),
              ('Paris', 'Paris'),
              ('Warsaw', 'Warsaw'),
              ('Moscow', 'Moscow'),
              ('Budapest', 'Budapest'),
              ('Roma', 'Roma'),
              ('Cairo', 'Cairo'),
              ('New York', 'New York'),
              ('Tokyo', 'Tokyo'),
              ('Sydney', 'Sydney'),
              ('Adamov', 'Adamov')
             ]

    # we have just one model in db
    cityName = models.CharField(max_length=30, verbose_name=('City Name'), choices=CITIES)

    # get city url by id for use in templates
    def getCityUrl(self):
        return reverse('city_detail_view', kwargs={'id': self.id})

    def __str__(self):
        return self.cityName

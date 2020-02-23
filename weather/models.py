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

    # get city url by id for use in templates
    def getCityUrl(self):
        return reverse('city_detail_view', kwargs={'id': self.id})

    def __str__(self):
        return self.cityName

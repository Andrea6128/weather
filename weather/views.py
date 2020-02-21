from django.shortcuts import render, get_object_or_404
# from django.db.models import Q
from .models import City

# Create your views here.

# homepage view
def home_view(request):
    queryset = City.objects.all()
    context = { 'CurrentCity': queryset,
                'CurrentTemp': City.currentTemp,
                'WeatherType': City.weatherType,
                'WeatherDesc': City.weatherDesc,
                'WindSpeed': City.windSpeed,
                'CurrentTime': City.currentTime,
              }
    return render(request, 'home_view.html', context)

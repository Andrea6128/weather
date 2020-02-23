from django.shortcuts import render, get_object_or_404
# from django.db.models import Q
from .models import City

# Create your views here.

# homepage view with list of cities and links to them
def home_view(request):
    queryset = City.objects.all()
    context = { 'cities': queryset }
    return render(request, 'home_view.html', context)

# city view by id for single city view
def city_id_view(request, id):
    city = get_object_or_404(City, id=id)
    context = { 'thiscity': city }
    return render(request, 'city.html', context)

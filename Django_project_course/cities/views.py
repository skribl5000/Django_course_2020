from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView


def home(request):
    cities = City.objects.all()
    ids = City.objects.all().values('id')
    return render(request,'cities/home.html',  {'object_list':cities, 'id_list': ids})

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'

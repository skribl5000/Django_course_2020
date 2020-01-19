from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CityForm


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid(): 
           print(form.cleaned_data)
    form = CityForm()
    cities = City.objects.all()
    ids = City.objects.all().values('id')
    return render(request,'cities/home.html',  {'object_list':cities, 'id_list': ids, 'form': form})
    # не забыть форму в контекст ->

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
  
class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy('city:home')



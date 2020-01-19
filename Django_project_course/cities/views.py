from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView
from .forms import HtmlForm


def home(request):
    if request.method == 'POST':
        form = HtmlForm(request.POST or None)
        if form.is_valid(): 
           print(form.cleaned_data)
    # form = HtmlForm()
    cities = City.objects.all()
    ids = City.objects.all().values('id')
    return render(request,'cities/home.html',  {'object_list':cities, 'id_list': ids, 'form': form})
    # не забыть форму в контекст ->

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'

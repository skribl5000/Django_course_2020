from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CityForm
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def home(request):
    cities = City.objects.all()
    ids = City.objects.all().values('id')
    paginator = Paginator(cities, 4)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    return render(request,'cities/home.html',  {'object_list':cities, 'id_list': ids, })
    # не забыть форму в контекст ->

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
  
class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно создан'

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно отредактирован'

class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно удален'

    # Вариант удаления сразу
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)
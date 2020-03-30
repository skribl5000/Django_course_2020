from django.shortcuts import render
from .models import Train
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import TrainForm

def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 4)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request,'trains/home.html',  {'object_list':trains})
    # не забыть форму в контекст ->

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'

class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/create.html"
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно создан'

class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/update.html"
    success_url = reverse_lazy('train:home')
    success_message = 'Пеозд успешно отредактирован'

class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    template_name = "trains/delete.html"
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно удален'

    # Вариант удаления сразу
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален')
        return self.post(request, *args, **kwargs)
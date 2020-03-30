from django import forms
from .models import Train
from cities.models import City

class TrainForm(forms.ModelForm): 
#     #form.ModelFrom - класс, который коннектится с моделью
#     # Модель прописывается в Meta-> model = ModelClassName без ().
    name = forms.CharField(label='Город', widget=forms.TextInput(
                                                attrs={'class':'form-control',
                                                'placeholder': 'Введите номер поезда'}))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-control',
    'placeholder': 'Откуда'}))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-control',
    'placeholder': 'Куда'}))
    travel_time = forms.IntegerField(label='Travel duration (hours)',widget=forms.NumberInput(
                                                attrs={'class':'form-control',
                                                'placeholder': 'Введите длительность поездки в часах'}))
#     # Переопределяем нашу переменную, связанную с моделью
#     # добавление аттрибутов в форму, widget=forms.TextInput(attrs={'class':'form-control'}).

    class Meta(object):
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')
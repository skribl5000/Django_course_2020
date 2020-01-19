from django import forms
from .models import City

class HtmlForm(forms.Form):
    name = forms.CharField(label='Город') 
    # Если поле необязательное - дописать аттрибут required = False.

class CityForm(forms.ModelForm): 
    #form.ModelFrom - класс, который коннектится с моделью
    # Модель прописывается в Meta-> model = ModelClassName без ().
    name = forms.CharField(label='Город', widget=forms.TextInput(
                                                attrs={'class':'form-control',
                                                'placeholder': 'Введите название города'}))
    # Переопределяем нашу переменную, связанную с моделью
    # добавление аттрибутов в форму, widget=forms.TextInput(attrs={'class':'form-control'}).

    class Meta(object):
        model = City
        fields = ('name',)
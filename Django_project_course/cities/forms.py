from django import forms

class HtmlForm(forms.Form):
    city_name = forms.CharField(label='Город') 
    # Если поле необязательное - дописать аттрибут required = False.
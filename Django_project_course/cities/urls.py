from django.contrib import admin
from django.urls import path
from .views import home
from .views import CityDetailView

urlpatterns = [
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('', home, name = 'home'),
]


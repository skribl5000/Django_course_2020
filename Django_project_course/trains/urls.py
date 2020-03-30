from django.contrib import admin
from django.urls import path
from .views import home 
from .views import TrainCreateView, TrainUpdateView, TrainDetailView, TrainDeleteView

urlpatterns = [
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name = 'delete'),
    path('', home, name = 'home'),
    path('add/', TrainCreateView.as_view(), name = 'add'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('homepage', views.Homepage, name='Homepage'),
]
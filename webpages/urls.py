
from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('youtube', views.youtube, name='youtubers'),
    path('contact', views.contact, name='contact'),

] 

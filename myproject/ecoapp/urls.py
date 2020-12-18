from django.urls import path
from .views import *



# app_name = 'ecoapp'


urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path
from .views import *



# app_name = 'ecoapp'


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name= 'about'),
    path('single_product/<int:id>/', single_product, name='single_product'),
]
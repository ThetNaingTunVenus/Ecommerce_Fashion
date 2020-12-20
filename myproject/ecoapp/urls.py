from django.urls import path
from .views import *



# app_name = 'ecoapp'


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name= 'about'),
    path('contact', contact, name= 'contact'),
    path('Search', SearchView, name='SearchView'),
    path('single_product/<int:id>/', single_product, name='single_product'),
]
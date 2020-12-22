from django.urls import path
from .views import *

urlpatterns = [
    path('404/', userprofile, name='404'),
]
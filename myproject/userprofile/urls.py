from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('user_profile/',user_profile, name='profile'),

]
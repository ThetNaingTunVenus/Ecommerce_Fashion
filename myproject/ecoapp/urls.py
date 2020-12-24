from django.urls import path
from .views import *



# app_name = 'ecoapp'


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name= 'about'),
    path('contact', contact, name= 'contact'),
    path('Search', SearchView, name='SearchView'),
    path('single_product/<int:id>/', single_product, name='single_product'),
    path('Add_to_Shopping_cart/<int:id>/', Add_to_Shopping_cart, name='Add_to_Shopping_cart'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('shopping_cart_delete/<int:id>/', shopping_cart_delete, name='shopping_cart_delete'),
    path('order_cart/', OrderCart, name='order_cart'),
    path('comment_add/<int:id>/', CommentAdd, name='comment_add'),
]
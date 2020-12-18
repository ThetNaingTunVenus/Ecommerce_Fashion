from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_at','update_at']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_at','update_at','image']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title','new_price','detail']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Category,Product,Images,Setting
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_at','update_at']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_at','update_at','image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title','new_price','detail']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ProductImageInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Setting)
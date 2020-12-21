from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category,Product,Images,Setting,HeadBanner,ContactMessage,ShopCart
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','phone','email','address']

class HeadBannerAdmin(admin.ModelAdmin):
    list_display = ['title','sale_offer','price']

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title','status','created_at','update_at']
#     list_filter = ['title', 'created_at']
#     list_per_page = 10
#     search_fields = ['title']

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'



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

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount']
    list_filter = ['user']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(HeadBanner,HeadBannerAdmin)
admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage)
admin.site.register(ShopCart,ShopCartAdmin)
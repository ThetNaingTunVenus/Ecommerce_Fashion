from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def about(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting':setting,
        'category':category,
    }
    return render(request,'frontend/about-us.html', context)

def home(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    banner_slide = Product.objects.all().order_by('id')[:2]
    lasted_product = Product.objects.all().order_by('-id')[:5]
    best_sellered = Product.objects.all().order_by('id')[:5]
    product = Product.objects.all()
    banner_image = HeadBanner.objects.all().order_by('id')[:2]
    context = {
        'setting':setting,
        'banner_slide':banner_slide,
        'lasted_product':lasted_product,
        'best_sellered':best_sellered,
        'product':product,
        'banner_image':banner_image,
        'category':category,
    }
    return render(request, 'frontend/index.html', context)



def single_product(request,id):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    product_detail = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'setting':setting,
        'product_detail':product_detail,
        'images':images,
        'category':category,
    }
    return render(request, 'frontend/single-product.html', context)
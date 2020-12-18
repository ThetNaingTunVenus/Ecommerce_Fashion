from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    setting = Setting.objects.get(id=1)
    banner_slide = Product.objects.all().order_by('id')[:2]
    lasted_product = Product.objects.all().order_by('-id')[:5]
    best_sellered = Product.objects.all().order_by('id')[:5]
    product = Product.objects.all()
    context = {
        'setting':setting,
        'banner_slide':banner_slide,
        'lasted_product':lasted_product,
        'best_sellered':best_sellered,
        'product':product,
    }
    return render(request, 'frontend/index.html', context)
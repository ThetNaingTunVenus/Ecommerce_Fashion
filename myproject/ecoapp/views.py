from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .models import *
from .forms import ContactMesageForm
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

def contact(request):
    if request.method == 'POST':
        form = ContactMesageForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # messages.success(request, 'Your Message Have been Sent')
            return HttpResponseRedirect(reversed('contact'))

    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    form = ContactMesageForm

    context = {
        'setting': setting,
        'category': category,
        'form':form,
    }
    return render(request,'frontend/contact.html', context)
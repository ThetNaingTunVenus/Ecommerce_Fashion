from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
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
    current_user = request.user
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    banner_slide = Product.objects.all().order_by('id')[:2]
    lasted_product = Product.objects.all().order_by('-id')[:5]
    best_sellered = Product.objects.all().order_by('id')[:5]
    product = Product.objects.all()
    banner_image = HeadBanner.objects.all().order_by('id')[:2]
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    context = {
        'setting':setting,
        'banner_slide':banner_slide,
        'lasted_product':lasted_product,
        'best_sellered':best_sellered,
        'product':product,
        'banner_image':banner_image,
        'category':category,
        'total_amount':total_amount,
        'cart_product':cart_product,
    }
    return render(request, 'frontend/index.html', context)



def single_product(request,id):
    current_user = request.user
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    product_detail = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    context = {
        'setting':setting,
        'product_detail':product_detail,
        'images':images,
        'category':category,
        'cart_product':cart_product,
        'total_amount':total_amount,
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
            messages.success(request, 'Your Message Have been Sent')
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

def SearchView(request):
    setting = Setting.objects.get(id=1)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                product = Product.objects.filter(title__icontains=query)
            else:
                product = Product.objects.filter(title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            context = {
                'category':category,
                'product':product,
                'query':query,
                'setting':setting,

            }
            return render(request,'frontend/searchproduct.html', context)
    return HttpResponseRedirect('home')

def Add_to_Shopping_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(product_id=id,user_id=current_user.id)
    if checking:
        control = 1
    else:
        control =0

    if request.method == 'POST':
        form = ShoppingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.filter(product_id=id,user_id=current_user.id)
                data.quantity = form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                messages.success(request, 'Add to Cart Successful')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.filter(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            messages.success(request, 'Add to Cart Successful')
        return HttpResponseRedirect(url)

def shopping_cart(request):
    current_user = request.user
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    context = {
        'setting':setting,
        'category':category,
        'current_user':current_user,
        'cart_product':cart_product,
        'total_amount':total_amount,
    }
    return render(request, 'frontend/shopping-cart.html', context)

def shopping_cart_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_product = ShopCart.objects.filter(id = id,user_id=current_user.id)
    cart_product.delete()
    messages.warning(request, 'Delete Product from Cart')
    return HttpResponseRedirect(url)
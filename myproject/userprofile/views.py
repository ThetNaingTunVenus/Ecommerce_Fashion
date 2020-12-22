from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages
from ecoapp.models import *
from .forms import *
from .models import *

# Create your views here.

def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
        # Return an 'invalid login' error message.
            messages.info(request, '--- Invalid Login, Please try Again!')
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category
    }
    return render(request, 'userprofile/login-register.html', context)


def user_register(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password1)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "userprofile/userimage.png"
            data.save()
            # messages.success(request, '--- Success!---')
            return redirect('home')
        else:
            messages.info(request,'--- Please try Again!---')
    else:
        form = SignupForm()

    context = {
        'setting': setting,
        'category': category,
        'form':form
    }
    return render(request, 'userprofile/user_register.html', context)

def user_profile(request):
    pass
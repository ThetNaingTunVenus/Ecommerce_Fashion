from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.forms import ModelForm,TextInput,NumberInput,EmailInput,PasswordInput,Select,FileInput
from .models import UserProfile

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=200, label='username', widget=forms.TextInput(attrs={'placeholder':'username'}))
    email = forms.EmailField(max_length=200, label='email',
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    first_name = forms.CharField(max_length=200, label='first_name',
                               widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=200, label='last_name',
                               widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets = {
            'password1':forms.PasswordInput(attrs={'placeholder':'Enter New Password',
                                                   'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                    'class': 'form-control'})
        }


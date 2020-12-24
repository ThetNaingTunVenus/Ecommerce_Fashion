from django import forms
from django.forms import TextInput,EmailInput

from .models import *

class ContactMesageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name' : TextInput(attrs={'class':'input','placeholder':'Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Message'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    cat_id = forms.IntegerField()

class ShoppingCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name','phone','address','city','country','transaction_id','transaction_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']
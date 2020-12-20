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
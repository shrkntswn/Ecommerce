from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from . models import *

class UserForm(UserCreationForm): #UserCreationForm ---> base class/// Abstract classes concept
    class Meta:
        model = User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password", max_length=100, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddressForm(forms.Form):
    class Meta:
        model = PrimaryAddress
        fields = '__all__'
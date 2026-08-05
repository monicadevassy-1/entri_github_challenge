from django import forms
from .models import Product,Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "phone", "bio"]
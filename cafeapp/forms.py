from django import forms
from django.forms import ModelForm

from cafeapp.models import Cafe, Product


class CafeCreationForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'description']

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'price', 'isSoldOut']


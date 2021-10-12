from django import forms
from django.forms import ModelForm

from cafeapp.models import Cafe, Order, Product


class CafeCreationForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'description']

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'price', 'isSoldOut']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'postal_code', 'city', 'paid']
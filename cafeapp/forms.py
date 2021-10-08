from django import forms
from django.forms import ModelForm

from cafeapp.models import Cafe, Order


class CafeCreationForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'description']

class ProductOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
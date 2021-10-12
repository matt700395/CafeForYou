from django import forms

from orderapp.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'postal_code', 'city', 'paid']
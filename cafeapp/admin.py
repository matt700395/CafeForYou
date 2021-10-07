from django.contrib import admin

# Register your models here.
from cafeapp.models import Cafe, Product, Order

admin.site.register(Cafe)
admin.site.register(Product)
admin.site.register(Order)

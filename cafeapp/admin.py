from django.contrib import admin

# Register your models here.
from cafeapp.models import Cafe, Product

admin.site.register(Cafe)
admin.site.register(Product)



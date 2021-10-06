from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cafe(models.Model):
    id = models.BigAutoField(help_text="Cafe ID", primary_key=True)
    owner = User()
    name = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=500, null=True)

class Product(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="cafe_product", on_delete=models.CASCADE)

    image = models.ImageField(upload_to='profile/', null=True)
    name = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=500, null=True)
    price = models.IntegerField()
    isSoldOut = models.BooleanField()

class Order(models.Model):
    id = models.BigAutoField(help_text="Order ID", primary_key=True)
    cafe = models.ForeignKey(Cafe, related_name="cafe_order", on_delete=models.CASCADE)

    user = User()
    product = Product()
    # name = models.CharField(max_length=20, label='제품명', null=True)
    # price = models.IntegerField(label='가격')
    # count = models.IntegerField(label='가격')



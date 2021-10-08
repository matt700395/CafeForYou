from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cafe(models.Model):
    id = models.BigAutoField(help_text="Cafe ID", primary_key=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cafe_owner')
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=500, null=True)

class Product(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="product", on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product/', null=True)
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=500, null=True)
    price = models.IntegerField()
    isSoldOut = models.BooleanField()
    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.BigAutoField(help_text="Order ID", primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    quantity = models.IntegerField(verbose_name="수량")


    # name = models.CharField(max_length=20, label='제품명', null=True)
    # price = models.IntegerField(label='가격')
    # count = models.IntegerField(label='가격')


#1. 카페 창설 접근권한 만들기
#2. order 페이지 생성
#3. 사장님 주문승인 리스트, 디테일 페이지 생성
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cafe(models.Model):
    id = models.BigAutoField(help_text="Cafe ID", primary_key=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cafe_owner')
    name = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=500, null=True)

class Product(models.Model):
    cafe = models.ForeignKey(Cafe, related_name="cafe_product", on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product/', null=True)
    name = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=500, null=True)
    price = models.IntegerField()
    isSoldOut = models.BooleanField()

class Order(models.Model):
    id = models.BigAutoField(help_text="Order ID", primary_key=True)
    cafe = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cafe_order')

    #count를 위한 model설정을 해야함!
    PERSON_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]
    personnel = models.CharField(max_length=2, choices=PERSON_CHOICES, default='1')
    #문제, 최대 개수의 제한이 문제, '1','1'은 줄일 수 없을까? 이게 최선은 아닌듯함
    #user_name = 유저 데이터도 받아서 카페 사장님이 확인할 수 있게끔 해야함

    # name = models.CharField(max_length=20, label='제품명', null=True)
    # price = models.IntegerField(label='가격')
    # count = models.IntegerField(label='가격')


#1. 카페 창설 접근권한 만들기
#2. order 페이지 생성
#3. 사장님 주문승인 리스트, 디테일 페이지 생성
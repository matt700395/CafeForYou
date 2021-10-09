from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cafe(models.Model):
    id = models.BigAutoField(help_text="Cafe ID", primary_key=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cafe')
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
    name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity



#1. 카페 창설 접근권한 만들기
#2. order 페이지 생성
#3. 사장님 주문승인 리스트, 디테일 페이지 생성
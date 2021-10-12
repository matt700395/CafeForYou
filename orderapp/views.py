from django.shortcuts import render

# Create your views here.
from cartapp.models import Cart
from orderapp.forms import OrderCreateForm
from orderapp.models import OrderItem


def order_create(request):
    cart = Cart(request)
    # user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():#정상적인 접근
            order = form.save()
            print("in form.is_valid!!")
            for item in cart:
                print("item: ", item)
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        else:#form에 문제있을 시
            print("=============================================\n\t\tform error\n=============================================")
            print(form.errors)
            print("=============================================\n")
        return render(request, 'orderapp/goodbye.html', {'order': order})#얘를 윗쪽 if에 넣고 여긴 에러페이지 넣어야함.
    else:
        form = OrderCreateForm()
    return render(request, 'orderapp/order.html', {'form': form})
from datetime import datetime, timedelta
from threading import Timer

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView

from cartapp.models import Cart
from orderapp.decorators import order_ownership_required
from orderapp.forms import OrderCreateForm
from orderapp.models import OrderItem, Order


class OrderListView(ListView):
    model = Order
    # context_object_name = 'order_list'
    ordering = ['-id']
    template_name = 'orderapp/list.html'

    def get_context_data(self, *, object_list=Order, **kwargs):
        #삭제 시간 조절하는곳
        object_list.objects.filter(created__lte=datetime.now() - timedelta(minutes=5)).delete()

        order_list = object_list.objects.filter(cafe=self.request.user.cafe)
        return super(OrderListView, self).get_context_data(order_list=order_list, **kwargs)

@method_decorator(order_ownership_required, 'get')
@method_decorator(order_ownership_required, 'post')
class OrderDeleteView(DeleteView):
    model = Order
    context_object_name = 'target_order'
    success_url = reverse_lazy('index')
    template_name = 'orderapp/delete.html'


def order_create(request):
    cart = Cart(request)
    # user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():#정상적인 접근
            temp_order = form.save(commit=False)
            temp_order.user = request.user
            # temp_order.cafe = cafe??
            temp_order = form.save()

            cafe = None
            for item in cart:
                print("item: ", item['product'].cafe)
                if cafe == None:
                    cafe = item['product'].cafe
                    temp_order.cafe = cafe
                    temp_order = form.save()
                elif cafe != item['product'].cafe:
                    print("======== 카페 정보가 다른 제품이 있습니다. =========\n")
                    temp_order.delete()
                    return render(request, 'error.html')

                OrderItem.objects.create(
                    order=temp_order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()
        else:#form에 문제있을 시
            print("=============================================\n\t\tform error\n=============================================")
            print(form.errors)
            print("=============================================\n")

        return render(request, 'orderapp/goodbye.html', {'order': temp_order})#얘를 윗쪽 if에 넣고 여긴 에러페이지 넣어야함.
    else:
        form = OrderCreateForm()
    return render(request, 'orderapp/order.html', {'form': form})


# ==paid 체크 없이 진행할 때==
# def order_create(request):
#     cart = Cart(request)
#     # user = get_object_or_404(User, id=user_id)
#     form = OrderCreateForm(request.POST)
#     if form.is_valid():#정상적인 접근
#
#         temp_order = form.save(commit=False)
#         temp_order.user = request.user
#         temp_order = form.save()
#         for item in cart:
#             print("item: ", item)
#             OrderItem.objects.create(
#                 order=temp_order,
#                 product=item['product'],
#                 price=item['price'],
#                 quantity=item['quantity']
#             )
#         cart.clear()
#     else:#form에 문제있을 시
#         print("=============================================\n\t\tform error\n=============================================")
#         print(form.errors)
#         print("=============================================\n")
#     return render(request, 'orderapp/goodbye.html', {'order': temp_order})#얘를 윗쪽 if에 넣고 여긴 에러페이지 넣어야함.
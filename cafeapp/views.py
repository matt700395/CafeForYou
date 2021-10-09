from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin, FormView

from cafeapp.decorators import cafe_ownership_required
from cafeapp.forms import CafeCreationForm, OrderCreateForm
from cafeapp.models import Cafe, Product, OrderItem
from cartapp.forms import CartAddProductForm
from cartapp.models import Cart


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CafeCreateView(CreateView):
    model = Cafe
    form_class = CafeCreationForm
    template_name = 'cafeapp/create.html'

    def form_valid(self, form):
        temp_cafe = form.save(commit=False)
        temp_cafe.owner = self.request.user
        temp_cafe.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.object.pk})


class CafeDetailView(DetailView):
    model = Cafe
    context_object_name = 'target_cafe'
    template_name = 'cafeapp/detail.html'
    def get_context_data(self, **kwargs):
        product_list = Product.objects.filter(cafe=self.object.pk)
        cart_product_form = CartAddProductForm()
        return super(CafeDetailView, self).get_context_data(product_list=product_list, cart_product_form=cart_product_form, **kwargs)

@method_decorator(cafe_ownership_required, 'get')
@method_decorator(cafe_ownership_required, 'post')
class CafeUpdateView(UpdateView):
    model = Cafe
    context_object_name = 'target_cafe'
    form_class = CafeCreationForm
    template_name = 'cafeapp/update.html'

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(cafe_ownership_required, 'get')
@method_decorator(cafe_ownership_required, 'post')
class CafeDeleteView(DeleteView):
    model = Cafe
    context_object_name = 'target_cafe'
    success_url = reverse_lazy('cafeapp:list')
    template_name = 'cafeapp/delete.html'

class CafeListView(ListView):
    model = Cafe
    context_object_name = 'cafe_list'
    ordering = ['-id']
    template_name = 'cafeapp/list.html'
    # def get_queryset(self):
    #     temp_list = Cafe.objects.filter()
    #
    #     page = int(self.request.GET.get('page', 1))
    #     paginator = Paginator(temp_list, 2)
    #     queryset = paginator.get_page(page)
    #
    #     return queryset


def order_create(request):
    cart = Cart(request)
    # user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():#에러  발생
            # temp_order = form.save(commit=False)
            # temp_order.name =
            order = form.save()
            # order = form.save(commit=False)
            # order.name = user.name
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
        else:
            print("===========")
            print(form.errors)
        return render(request, 'cafeapp/goodbye.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'cafeapp/order.html', {'form': form})
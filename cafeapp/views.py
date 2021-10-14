from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin, FormView

from cafeapp.decorators import cafe_ownership_required, product_ownership_required
from cafeapp.forms import CafeCreationForm, ProductCreationForm
from cafeapp.models import Cafe, Product
from cartapp.forms import CartAddProductForm
from cartapp.models import Cart


class LoginRequired(AccessMixin):
    """로그인, 프로필 체크 클래스"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        try:
            request.user.profile
        except:
            return render(request, 'no_profile.html')
        return super().dispatch(request, *args, **kwargs)


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class CafeCreateView(LoginRequired, CreateView):
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


class CafeDetailView(LoginRequired, DetailView):
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
    success_url = reverse_lazy('index')
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

# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class ProductCreateView(LoginRequired, CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'cafeapp/create_product.html'

    def form_valid(self, form):
        temp_product = form.save(commit=False)
        temp_product.cafe = self.request.user.cafe
        temp_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.request.user.cafe.pk})


@method_decorator(product_ownership_required, 'get')
@method_decorator(product_ownership_required, 'post')
class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = 'target_product'
    form_class = ProductCreationForm
    template_name = 'cafeapp/update_product.html'

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.request.user.cafe.pk})


@method_decorator(product_ownership_required, 'get')
@method_decorator(product_ownership_required, 'post')
class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'target_product'
    template_name = 'cafeapp/delete_product.html'

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.request.user.cafe.pk})



from django.conf.urls import url
from django.urls import path

from cafeapp import views
from cafeapp.views import CafeCreateView, CafeUpdateView, CafeDetailView, CafeDeleteView, CafeListView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = "cafeapp"

urlpatterns = [
    path('create/', CafeCreateView.as_view(), name='create'),
    path('update/<int:pk>', CafeUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', CafeDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', CafeDeleteView.as_view(), name='delete'),

    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

    path('list/', CafeListView.as_view(), name='list'),
    url(r'^order/$', views.order_create, name='order_create'),
    # url(r'^order/(?P<user_id>\d+)/$', views.order_create, name='order_create'),

]
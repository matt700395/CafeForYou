from django.conf.urls import url
from django.urls import path

from . import views
from .views import OrderListView, OrderDeleteView

app_name = 'orderapp'

urlpatterns = [
    url(r'^order/$', views.order_create, name='order_create'),
    path('list/', OrderListView.as_view(), name='list'),
    path('delete/<int:pk>', OrderDeleteView.as_view(), name='delete'),
]
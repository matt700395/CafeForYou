from django.conf.urls import url
from . import views

app_name = 'orderapp'

urlpatterns = [
    url(r'^order/$', views.order_create, name='order_create'),

]
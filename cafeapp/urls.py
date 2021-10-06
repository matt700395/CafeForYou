from django.urls import path

from cafeapp.views import CafeCreateView, CafeUpdateView, CafeDetailView, CafeDeleteView, CafeListView

app_name = "cafeapp"

urlpatterns = [
    path('create/', CafeCreateView.as_view(), name='create'),
    path('update/<int:pk>', CafeUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', CafeDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', CafeDeleteView.as_view(), name='delete'),
    path('list/', CafeListView.as_view(), name='list'),
]
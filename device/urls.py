from django.urls import path
from device import views

urlpatterns = [
    path("list", views.DeviceView.as_view(), name='device_list'),
    path("list/<int:pk>", views.DeviceDetailView.as_view(), name='device_detail'),
]
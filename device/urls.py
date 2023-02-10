from django.urls import path
from device.views import DeviceView

urlpatterns = [
    path("list", DeviceView.as_view(), name='device_list'),
]
from django.shortcuts import render
from rest_framework import generics
from device.models import Device
from device.serializers import DeviceSerializer
# Create your views here.


class DeviceView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer




from django.shortcuts import render
from rest_framework import generics
from device.models import Device
from device.serializers import DeviceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DeviceView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetailView(APIView):
    def get_object(self, pk):
        try:
            device = Device.objects.get(id=pk)
            
        except Device.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return device

        
    def get(self, request, pk):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)



        




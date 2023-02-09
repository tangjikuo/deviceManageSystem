from django.db import models

# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=125, help_text='设备名称')
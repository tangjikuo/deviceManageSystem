from django.db import models

# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=125, help_text='设备名称')
    device_manager = models.CharField(max_length=25, help_text='设备管理员')
    device_owner = models.CharField(max_length=25, help_text='设备管当前所属')
    create_time = models.DateTimeField(auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField(auto_now=True, help_text='设备更新时间')
    borrow_time = models.DateTimeField(help_text='设备借出时间', null=True)
    
    class Meta:
        db_table = "devices"
        

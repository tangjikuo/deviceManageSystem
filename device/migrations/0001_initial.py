# Generated by Django 4.1.6 on 2023-02-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("device_name", models.CharField(help_text="设备名称", max_length=125)),
                ("device_manager", models.CharField(help_text="设备管理员", max_length=25)),
                ("device_owner", models.CharField(help_text="设备管当前所属", max_length=25)),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, help_text="create time"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, help_text="设备更新时间"),
                ),
                ("borrow_time", models.DateTimeField(help_text="设备借出时间", null=True)),
            ],
            options={"db_table": "devices",},
        ),
    ]

# Generated by Django 4.2 on 2025-02-20 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_deliveryaddresss_delete_deliveryaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeliveryAddresss',
            new_name='DeliveryAddress',
        ),
    ]

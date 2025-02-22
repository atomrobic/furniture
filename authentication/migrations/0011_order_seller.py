# Generated by Django 5.1.6 on 2025-02-16 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_complaint_complaint_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders_seller', to='authentication.seller'),
            preserve_default=False,
        ),
    ]

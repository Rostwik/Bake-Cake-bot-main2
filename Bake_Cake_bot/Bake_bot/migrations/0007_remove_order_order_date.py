# Generated by Django 3.2.7 on 2021-10-27 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bake_bot', '0006_rename_deliivery_address_order_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-27 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0031_order_wholesaler_show_delete_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='wholesaler_show',
        ),
    ]

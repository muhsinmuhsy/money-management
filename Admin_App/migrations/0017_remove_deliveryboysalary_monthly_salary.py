# Generated by Django 4.2.1 on 2023-07-25 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0016_deliveryboysalary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboysalary',
            name='monthly_salary',
        ),
    ]

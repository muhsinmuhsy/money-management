# Generated by Django 4.2.1 on 2023-07-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0018_alter_deliveryboysalary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryboysalary',
            name='salary_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
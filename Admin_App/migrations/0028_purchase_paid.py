# Generated by Django 4.2.1 on 2023-07-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0027_purchase_wholesaler_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]

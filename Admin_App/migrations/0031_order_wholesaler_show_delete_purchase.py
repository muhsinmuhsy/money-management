# Generated by Django 4.2.1 on 2023-07-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0030_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='wholesaler_show',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]

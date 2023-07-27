# Generated by Django 4.2.1 on 2023-07-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0033_order_wholesaler_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='wholesaler_show',
            field=models.CharField(choices=[('SHOW', 'SHOW'), ('UNSHOW', 'UNSHOW')], default='SHOW', max_length=100),
        ),
    ]
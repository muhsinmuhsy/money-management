# Generated by Django 4.2.1 on 2023-07-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0011_order_money_collected_order_money_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='confirm_cancel_pending',
            field=models.CharField(blank=True, choices=[('CONFIRM', 'CONFIRM'), ('CANCEL', 'CANCEL'), ('PENDING', 'PENDING'), ('COMPLEATED', 'COMPLEATED')], max_length=500, null=True),
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-21 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Admin_App', '0002_rename_address_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('money_type', models.CharField(blank=True, choices=[('AED to INR', 'AED to INR'), ('INR to AED', 'INR to AED')], max_length=500, null=True)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('delivery_type', models.CharField(blank=True, choices=[('HOME', 'HOME'), ('BANK', 'BANK')], max_length=500, null=True)),
                ('home_name', models.CharField(blank=True, max_length=500, null=True)),
                ('home_mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('home_address', models.CharField(blank=True, max_length=500, null=True)),
                ('person_name', models.CharField(blank=True, max_length=500, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=500, null=True)),
                ('account', models.CharField(blank=True, max_length=500, null=True)),
                ('ifse', models.CharField(blank=True, max_length=500, null=True)),
                ('collector_name', models.ForeignKey(limit_choices_to={'is_collector': True}, on_delete=django.db.models.deletion.CASCADE, related_name='collector_orders', to=settings.AUTH_USER_MODEL)),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin_App.customer')),
                ('delivery_boy_name', models.ForeignKey(blank=True, limit_choices_to={'is_delivery_boy': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_boy_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
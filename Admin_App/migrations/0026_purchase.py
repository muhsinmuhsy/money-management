# Generated by Django 4.2.1 on 2023-07-27 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Admin_App', '0025_order_profit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('delivery_boy_name', models.ForeignKey(blank=True, limit_choices_to={'is_delivery_boy': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

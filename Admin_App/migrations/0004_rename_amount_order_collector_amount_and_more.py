# Generated by Django 4.2.1 on 2023-07-21 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Admin_App', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='collector_amount',
        ),
        migrations.AlterField(
            model_name='order',
            name='collector_name',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_collector': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collector_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=500)),
                ('Address', models.CharField(max_length=500)),
            ],
        ),
    ]

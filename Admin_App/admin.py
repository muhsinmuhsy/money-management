from django.contrib import admin
from Admin_App.models import *
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]


@admin.register(DeliveryBoySalary)
class DeliveryBoySalaryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeliveryBoySalary._meta.fields]
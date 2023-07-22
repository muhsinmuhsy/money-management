from django.contrib import admin
from Admin_App.models import *
# Register your models here.
@admin.register(Customer)
class CustomersModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]


@admin.register(Order)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
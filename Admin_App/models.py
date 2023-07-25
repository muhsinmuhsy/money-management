from django.db import models
from U_Auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    def __str__ (self):
        return self.name

class Wholesaler(models.Model):
    name = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    def __str__ (self):
        return self.name


class Order(models.Model):
    MONEY_TYPE = (
        ('AED to INR' , 'AED to INR'),      
        ('INR to AED' , 'INR to AED'),
    )
    DELIVERY_TYPE = (
        ('HOME' , 'HOME'),
        ('BANK' , 'BANK'),
        
    )
    DELIVERY_STATUS = (
        ('CONFIRM', 'CONFIRM'),
        ('CANCEL', 'CANCEL'),
        ('PENDING', 'PENDING'),
        ('COMPLEATED', 'COMPLEATED')
    )
    date = models.DateField(null=True, blank=True)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    money_type = models.CharField(max_length=500, choices=MONEY_TYPE, null=True, blank=True)
    mrp = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField( null=True, blank=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)

    collector_amount = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    collector_name = models.ForeignKey(
        User,
        limit_choices_to={'is_collector': True},
        on_delete=models.CASCADE,related_name='collector_orders',
        null=True, blank=True
    )
    name = models.CharField(max_length=500, null=True, blank=True)
    mobile = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    # Collected
    money_collected = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    money_pending = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    

    delivery_type = models.CharField(max_length=500, choices=DELIVERY_TYPE, null=True, blank=True)
    delivery_boy_amount = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)

    delivery_boy_name = models.ForeignKey(
        User,
        limit_choices_to={'is_delivery_boy': True},
        related_name='delivery_boy_orders',
        on_delete=models.CASCADE, null=True, blank=True
    )

    # HOME
    
    wholesaler_name = models.ForeignKey(Wholesaler, on_delete=models.CASCADE, null=True, blank=True)

    home_name = models.CharField(max_length=500, null=True, blank=True)
    home_mobile = models.CharField(max_length=500, null=True, blank=True)
    home_address = models.CharField(max_length=500, null=True, blank=True)

    # BANK
    person_name = models.CharField(max_length=500, null=True, blank=True)
    bank_name = models.CharField(max_length=500, null=True, blank=True)
    account = models.CharField(max_length=500, null=True, blank=True)
    ifse = models.CharField(max_length=500, null=True, blank=True)

    # Delivery boy status
    delivery_status = models.CharField(max_length=500, choices=DELIVERY_STATUS, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    def __str__ (self):
        return self.name

class DeliveryBoySalary(models.Model):
    delivery_boy_name = models.ForeignKey(
        User,
        limit_choices_to={'is_delivery_boy': True},
        on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField(null=True, blank=True)
    salary_amount = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
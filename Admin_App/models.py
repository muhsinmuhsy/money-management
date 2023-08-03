from django.db import models
from U_Auth.models import User
from decimal import Decimal

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
    DISPLAY = (
        ('SHOW' , 'SHOW'),      
        ('UNSHOW' , 'UNSHOW'),
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
    # money_type = models.CharField(max_length=500, choices=MONEY_TYPE, null=True, blank=True)
    
    # Purcahse
    purchase_mrp = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    purchase_quantity = models.PositiveIntegerField( null=True, blank=True)
    purchase_total = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)

    # Sales Information
    mrp = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField( null=True, blank=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)

    profit = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)


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
    wholesaler_paid = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    wholesaler_show = models.CharField(max_length=100, choices= DISPLAY, default="UNSHOW")
    

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

    def __str__(self):
        return f"Order #{self.id}"
    
    # profit saving
    def save(self, *args, **kwargs):
        if self.purchase_total is not None and self.total is not None:
            try:
                purchase_total = Decimal(self.purchase_total)
                total = Decimal(self.total)
                self.profit = total - purchase_total
            except (ValueError, TypeError):
                # Handle the case where purchase_total or total is not a valid number
                self.profit = None
        else:
            self.profit = None
        super(Order, self).save(*args, **kwargs)


        

class DeliveryBoySalary(models.Model):
    delivery_boy_name = models.ForeignKey(
        User,
        limit_choices_to={'is_delivery_boy': True},
        on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField(null=True, blank=True)
    salary_amount = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)




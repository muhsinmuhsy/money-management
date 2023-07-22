from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_collector = models.BooleanField(default=False)
    is_delivery_boy = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=20)

    def __str__ (self):
        return self.username
    


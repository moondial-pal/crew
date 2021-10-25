from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_service_date = models.DateField()
    services_per_month= models.CharField(max_length=100)
    service_duration = models.CharField(max_length=100)
    images = models.ImageField()
    notes = models.CharField(max_length=2000)

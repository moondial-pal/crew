from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_service_date = models.DateField()
    services_per_month = models.IntegerField(max_length=100)
    service_duration = models.IntegerField(max_length=100)
    images = models.ImageField(blank=True)
    notes = models.CharField(blank=True, max_length=2000)

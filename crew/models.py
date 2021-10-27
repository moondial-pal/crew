from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_service_date = models.DateField()

    # change to integer field
    services_per_month = models.CharField(max_length=100)
    # change to integer field
    service_duration = models.CharField(max_length=100)
    # make optional
    images = models.ImageField()
    # make optional
    notes = models.CharField(max_length=2000)

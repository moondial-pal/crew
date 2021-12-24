from address.models import AddressField
from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Truck(models.Model):
    truck_id = models.IntegerField()
    truck_email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Client(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    first_service_date = models.DateField()
    services_per_month = models.IntegerField()
    service_duration = models.IntegerField()
    images = models.ImageField(blank=True, upload_to="crew/media/images/")
    notes = models.CharField(blank=True, max_length=2000)


class Service(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class MultipleImage(models.Model):
    images = models.FileField()    

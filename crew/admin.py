from django.contrib import admin
from crew.models import Client
from crew.models import Truck
from crew.models import Service
from crew.models import MultipleImage

# Register your models here.

admin.site.register(Client)
admin.site.register(Truck)
admin.site.register(Service)
admin.site.register(MultipleImage)

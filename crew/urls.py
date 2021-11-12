from django.urls import path

from crew.views import index, clients

app_name = "crew"

urlpatterns = [
    path("", index, name="index"),
    path("clients/", clients, name="clients"),
    path("clients/<int:client_id>/details", clients, name="client"),
]

from django.urls import path

from crew.views import index, client

app_name = "crew"

urlpatterns = [
    path("", index, name="index"),
    path("client/<int:client_id>", client, name="client"),
]

from django.urls import path

from crew.views import index

app_name = "crew"

urlpatterns = [
    path("", index, name="index"),
]

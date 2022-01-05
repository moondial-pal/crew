from django.urls import path

from . import views

from crew.views import index, clients, client_details, route_schedule

from django.conf import settings

from django.conf.urls.static import static

app_name = "crew"

urlpatterns = [
    path("", index, name="index"),
    path("clients/", clients, name="clients"),
    path("clients/<int:client_id>/details", client_details, name="client_details"),
    path("client_details", views.upload, name="upload"),
    path("route_schedule/", route_schedule, name="route_schedule"),
    path("<int:year>/<str:month>/", route_schedule, name="route_schedule"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

from django.shortcuts import render
from crew.models import Client

# Create your views here.


def index(request):
    # get a list of all clients
    clients = Client.objects.all()

    return render(
        request, "index.html",
        {
            "test_var": "hello world",
            "clients": clients
        },
    )


def client(request, client_id):
    # get a specific client
    client = Client.objects.get(id=client_id)

    return render(
        request, "client.html",
        {
            "client": client
        },
    )

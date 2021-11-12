from django.shortcuts import render
from crew.models import Client

# Create your views here.

def index(request):
    return render(
            request, "index.html",
        {
            "test_var": "hello world",
        },
    )


def clients(request):
    clients = Client.objects.all()
    return render(
            request, "clients.html",
            {
                "clients": clients
            },
    )

def client_details(request, client_id):
    # get a specific client
    client = Client.objects.get(id=client_id)

    return render(
            request, "client_details.html",
            {
                "client_details": client
            },
    )






#    client = Client.objects.get(id=client_id)

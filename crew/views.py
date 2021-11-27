from django.shortcuts import render
from crew.models import Client, Truck, Service
from crew.forms import PersonForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

def index(request):
    form = PersonForm()
    return render(
            request, 
            "index.html",
        {
            "test_var": "hello",
            "form": form,
        },
    )


def clients(request):
    truck = Truck.objects.filter(user=request.user).first()
    clients = Client.objects.filter(truck=truck)

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

def route_schedule(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M: %p ')

    services = Service.objects.filter(date=datetime.today())
    ## filter service based on clients that belong to truck


    return render(
            request, "route_schedule.html",
            {
            "services": services,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time,
            }
    )





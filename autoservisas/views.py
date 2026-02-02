from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Order, OrderLine, Service

def index(request):

    context = {
        'num_services': Service.objects.count(),
        'num_cars': Car.objects.all().count(),
        'num_orders': Order.objects.all().count(),
    }

    return render(request, template_name="index.html", context=context)


def dashboard(request):
    context = {
        'cars': Car.objects.all(),
    }
    return render(request, template_name="dash.html", context=context)

def car(request, car_id):
    # car = Car.objects.get(pk=car_id)
    context = {
        'cars': Car.objects.all(),
        'car': Car.objects.get(pk=car_id)
    }
    return render(request, template_name="car.html", context=context)

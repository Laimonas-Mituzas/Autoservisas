from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Order, OrderLine, Service
from django.views import generic

def index(request):
    context = {
        'cars': Car.objects.all(),
    }

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
    return render(request, template_name="cars.html", context=context)


def cars(request):
    return render(request, template_name="cars.html", context={'cars': Car.objects.all()})


def car(request, car_id):
    return render(request, template_name="car.html", context={'car': Car.objects.get(pk=car_id)})

# Order listas
class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'


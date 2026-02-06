from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Order, OrderLine, Service
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):

    context = {
        'num_services': Service.objects.count(),
        'num_cars': Car.objects.all().count(),
        'num_orders': Order.objects.all().count(),


    }
    return render(request, template_name="index.html", context=context)


def dashboard(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'cars': Car.objects.all(),
        'num_visits': num_visits,
    }
    return render(request, template_name="dash.html", context=context)


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    return render(request, template_name="cars.html", context={'cars': paged_cars})
    # return render(request, template_name="cars.html", context={'cars': Car.objects.all()})


def car(request, car_id):
    return render(request, template_name="car.html", context={'car': Car.objects.get(pk=car_id)})

# Order listas
class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
    paginate_by = 3

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'

def search(request):
    query = request.GET.get('query')
    car_search_results = Car.objects.filter(Q(make__icontains=query) |
                                            Q(model__icontains=query) |
                                            Q(license_plate__icontains=query) |
                                            Q(vin_code__icontains=query) |
                                            Q(client_name__icontains=query))
    context = {
        "query": query,
        "cars": car_search_results,
    }
    return render(request, template_name="search.html", context=context)
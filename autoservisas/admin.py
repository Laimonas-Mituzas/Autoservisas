from django.contrib import admin
from .models import Car, Order, OrderLine, Service


class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car','date']

    inlines = [OrderLineInLine]

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order','service','quantity']

class CarAdmin(admin.ModelAdmin):
    list_display = ['model','client_name','license_plate','vin_code']
    list_filter = ['client_name','make','model']
    search_fields = ['license_plate','vin_code']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','price']

# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Service, ServiceAdmin)



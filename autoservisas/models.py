from django.db import models

class Car(models.Model):
    make = models.CharField(verbose_name="Markė", max_length=100)
    model = models.CharField(verbose_name="Modelis", max_length=100)
    license_plate = models.CharField(verbose_name="Numeris", max_length=100)
    vin_code = models.CharField(verbose_name="VIN", max_length=100)
    client_name = models.CharField(verbose_name="Klientas", max_length=100)

    def __str__(self):
        return self.license_plate

class Order(models.Model):
    date = models.DateField(verbose_name="Data", max_length=10)
    car_id = models.ForeignKey(to="Car", verbose_name="Auto", on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return self.date

class OrderLine(models.Model):
    order_id = models.ForeignKey(to="Order", verbose_name="Uzsakymas", on_delete=models.SET_NULL, null=True )
    service_id = models.ForeignKey(to="Service", verbose_name="Paslauga", on_delete=models.SET_NULL, null=True )
    quantity = models.IntegerField(verbose_name="Kiekis")

    def __str__(self):
        return self.order_id

class Service(models.Model):
    name = models.CharField(verbose_name="Paslauga", max_length=100)
    price = models.FloatField(verbose_name="Kaina", max_length=100)

    def __str__(self):
        return self.name





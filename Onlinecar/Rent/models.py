from datetime import datetime

from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    car_name = models.CharField(max_length=120)
    brand_nme = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Modd = models.CharField(max_length=120)
    seat_Select = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    lw_km = models.CharField(max_length=120)
    Hi_km = models.CharField(max_length=120)
    price_high = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images")
    active_status = models.IntegerField(default=1)

    def __str__(self):
        return self.car_name


class Orders(models.Model):
    Person_name = models.CharField(max_length=120)
    Age = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    Address = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    user = models.CharField(max_length=15)
    car_id = models.IntegerField()
    orderDate = models.DateField(default=datetime.now, blank=True)
    choice = (
        ('ordered', 'ordered'),
        ('recieved', 'recieved'),
        ('cancelled', 'cancelled'),
    )
    active_state = models.IntegerField(default=1)
    status = models.CharField(max_length=120, choices=choice, default='ordered')

    def __str__(self):
        return self.Person_name
# class CheckDatemod(models.Model):
#     from_datt = models.DateField()
#     to_datt = models.DateField()

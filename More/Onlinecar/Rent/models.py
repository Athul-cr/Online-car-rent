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

    def __str__(self):
        return self.car_name

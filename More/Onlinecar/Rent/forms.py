from django.forms import ModelForm
from Rent.models import Brand,Car
from django import forms

class BrandFormm(ModelForm):
    class Meta:
        model=Brand
        fields = "__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={"class":"form-control"})
        }
class CarRentFormm(ModelForm):
    class Meta:
        model=Car
        fields = "__all__"
        widgets={
            "car_name": forms.TextInput(attrs={"class": "form-control"}),
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),
            "Modd": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "lw_km": forms.TextInput(attrs={"class": "form-control"}),
            "Hi_km": forms.TextInput(attrs={"class": "form-control"}),
            "price_high": forms.TextInput(attrs={"class": "form-control"}),

        }
from django.forms import ModelForm
from Rent.models import Brand, Car, Orders
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BrandFormm(ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            "brand_name": forms.TextInput(attrs={"class": "form-control"})
        }


class CarRentFormm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "car_name": forms.TextInput(attrs={"class": "form-control"}),
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),
            "Modd": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "lw_km": forms.TextInput(attrs={"class": "form-control"}),
            "Hi_km": forms.TextInput(attrs={"class": "form-control"}),
            "price_high": forms.TextInput(attrs={"class": "form-control"}),

        }


class SearchForm(forms.Form):
    brand_name = forms.CharField(max_length=120)


class RegisterationFm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.TextInput(attrs={"class": "form-control"}),
            "password2": forms.TextInput(attrs={"class": "form-control"}),

        }


# class OrderForm(ModelForm):
#     class Meta:
#         model = Orders
#         fields = "__all__"
#         widgets = {
#             "Person_name": forms.TextInput(attrs={"class": "form-control"}),
#             "Age": forms.TextInput(attrs={"class": "form-control"}),
#             "phone_number": forms.TextInput(attrs={"class": "form-control"}),
#             "Address": forms.TextInput(attrs={"class": "form-control"}),
#
#         }
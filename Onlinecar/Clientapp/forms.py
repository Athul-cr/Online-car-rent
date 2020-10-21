from django.forms import ModelForm
from Rent.models import Orders
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"
        widgets = {
            "Person_name": forms.TextInput(attrs={"class": "form-control"}),
            "Age": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "Address": forms.TextInput(attrs={"class": "form-control"}),


        }
class OrderUpdatefm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"
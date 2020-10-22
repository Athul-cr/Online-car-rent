from Leaveapp.models import Leavemgmnt
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class Leavemgmntfm(ModelForm):
    class Meta:
        model = Leavemgmnt
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control"}),
            "desgination":forms.TextInput(attrs={"class":"form-control"}),
            "toDate": forms.TextInput(attrs={"class": "form-control"}),
            "AplyDate": forms.TextInput(attrs={"class": "form-control"}),
            "toDate": forms.TextInput(attrs={"class": "form-control"}),
            "Reason": forms.TextInput(attrs={"class": "form-control"}),
            "days": forms.TextInput(attrs={"class": "form-control"}),
            "leave_status": forms.HiddenInput(attrs={"class": "form-control"}),
            "Total_leave": forms.TextInput(attrs={"readonly": "readonly","class": "form-control"}),

        }

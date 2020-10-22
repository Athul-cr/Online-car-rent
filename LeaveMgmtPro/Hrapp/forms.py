from django.forms import ModelForm
from Hrapp.models import HrUserMod
from Leaveapp.models import Leavemgmnt
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Leaveapp.forms import Leavemgmntfm


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


class HrUserFm(ModelForm):
    class Meta:
        model = HrUserMod
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control"}),
            "Position": forms.TextInput(attrs={"class": "form-control"}),
            "Worklocation": forms.TextInput(attrs={"class": "form-control"}),
            "Edu_qual": forms.TextInput(attrs={"class": "form-control"}),
            "Age": forms.TextInput(attrs={"class": "form-control"}),
            "Startdate": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.TextInput(attrs={"class": "form-control"}),
            "Experience": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "wrkmail": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),


        }


class LeaveConfirmfm(ModelForm):
    class Meta:
        model = Leavemgmnt
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control"}),
            "desgination": forms.TextInput(attrs={"class": "form-control"}),
            "AplyDate": forms.TextInput(attrs={"class": "form-control"}),
            "toDate": forms.TextInput(attrs={"class": "form-control"}),
            "Reason": forms.TextInput(attrs={"class": "form-control"}),
            "days": forms.TextInput(attrs={"class": "form-control"}),
            "Total_leave": forms.TextInput(attrs={"class": "form-control"}),

        }

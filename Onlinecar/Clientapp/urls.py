from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from Clientapp.views import Userindex, RegistraionUser, LogincheckUser, ViewOrderUser, orderDetails
from Rent.views import OrderCreate

urlpatterns = [

    path('', lambda request: render(request, "Clientapp/userbase.html")),
    path('userindex', Userindex, name="userindex"),
    path('createuser<int:pk>', OrderCreate, name="OrderCreate"),
    path('Register', RegistraionUser, name="RegistraionUser"),
    path('Logincheckuser', LogincheckUser, name="LogincheckUser"),
    path('vieworder', ViewOrderUser, name="ViewOrderUser"),
    path('orderdetails<int:pk>', orderDetails, name="orderDetails")

]

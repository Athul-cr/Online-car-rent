from django.contrib import admin
from django.urls import path
from .views import RegistraionCreate, Loginhr, Createuser, Hrhome, Leaveconfirm,Landing,EditUser,DeletePro,DeleteStatus,LogOuthr

urlpatterns = [
    path("register", RegistraionCreate, name="RegistraionCreate"),
    path("login", Loginhr, name="Loginhr"),
    path("create", Createuser, name="Createuser"),
    path('status<int:pk>', Hrhome, name="Hrhome"),
    path('leave<int:pk>', Leaveconfirm, name="Leaveconfirm"),
    path('',Landing,name="Landing"),
    path('Editempl<int:pk>',EditUser,name="EditUser"),
    path('dele<int:pk>',DeletePro,name="DeletePro"),
    path("deletestatus<int:pk>",DeleteStatus,name="DeleteStatus"),
    path("logot",LogOuthr,name="LogOuthr")
]

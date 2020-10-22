
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import Userhome,Register,Logincheck,Viewstatus,Landinguser,IndexUser,LogOut

urlpatterns = [
    path("User",Userhome,name="Userhome"),
    path("Register",Register,name="Register"),
    path("Login",Logincheck,name="Logincheck"),
    path("view<int:pk>",Viewstatus,name="Viewstatus"),
    path("",Landinguser,name="Landinguser"),
    path("index",IndexUser,name="IndexUser"),
    path("log",LogOut,name="LogOut")

]

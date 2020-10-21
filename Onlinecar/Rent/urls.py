
from django.contrib import admin
from django.urls import path
from Rent.views import createBrand,BrandEdit,BrandDel,HomeCheck,Carcreate,index,CarEdit,DeleteCar,RegistraionCreate,Logincheck,OrderCreate,ViewOrder,Logout,orderDetails

urlpatterns = [
    path("create",createBrand,name="createBrand"),
    path("edit<int:pk>",BrandEdit,name="BrandEdit"),
    path("dele<int:pk>",BrandDel,name="BrandDel"),
    path("homecheck",HomeCheck,name="HomeCheck"),
    path('createcar',Carcreate,name="Carcreate"),
    path('',index,name="index"),
    path('Caredit<int:pk>',CarEdit,name="caredit"),
    path('deletcar<int:pk>',DeleteCar,name="DeleteCar"),
    path('register',RegistraionCreate,name="RegisterCreate"),
    path('loginpage',Logincheck,name="Logincheck"),
    path('createuser<int:pk>',OrderCreate,name="OrderCreate"),
    path('view',ViewOrder,name="vieworder"),
    path('logout',Logout,name="logout"),
    path('orderdetails<int:pk>',orderDetails,name="orderDetails")


]

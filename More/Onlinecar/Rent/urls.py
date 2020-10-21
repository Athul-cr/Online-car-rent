
from django.contrib import admin
from django.urls import path
from Rent.views import createBrand,BrandEdit,BrandDel,HomeCheck,Carcreate

urlpatterns = [
    path("create",createBrand,name="createBrand"),
    path("edit<int:pk>",BrandEdit,name="BrandEdit"),
    path("dele<int:pk>",BrandDel,name="BrandDel"),
    path("",HomeCheck,name="HomeCheck"),
    path('createcar',Carcreate,name="Carcreate")

]

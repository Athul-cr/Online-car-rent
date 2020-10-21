from django.shortcuts import render, redirect
from Rent.models import Brand,Car
from Rent.forms import BrandFormm,CarRentFormm
# Create your views here.

def createBrand(request):
    form=BrandFormm()
    context={}
    context['form']=form
    qs=Brand.objects.all()
    context['qs']=qs
    if request.method == "POST":
        form=BrandFormm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createBrand")
    return render(request,"Rent/CreateBrand.html",context)

def BrandEdit(request,pk):
    form=Brand.objects.get(id=pk)
    form=BrandFormm(instance=form)
    context={}
    context['form']=form
    if request.method == "POST":
        form = Brand.objects.get(id=pk)
        form = BrandFormm(instance=form,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createBrand")
    return render(request,"Rent/BrandEdit.html",context)
def BrandDel(request,pk):
    dele=Brand.objects.get(id=pk)
    dele.delete()
    qs=BrandFormm()
    context={}
    context['del']=qs
    qs=Brand.objects.all()
    context['brand']=qs
    return redirect("createBrand")
def HomeCheck(request):
    return render(request,"Rent/base.html")

def Carcreate(request):
    form=CarRentFormm()
    context={}
    context['form']=form
    qs=Car.objects.all()
    context['cars']=qs
    if request.method == "POST":
        form=CarRentFormm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Carcreate")
    return render(request,"Rent/Carcreate.html",context)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from Rent.models import Brand, Car, Orders
from Rent.forms import BrandFormm, CarRentFormm, SearchForm, RegisterationFm
from Clientapp.forms import OrderForm,OrderUpdatefm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="Logincheck")
def createBrand(request):
    form = BrandFormm()
    context = {}
    context['form'] = form
    qs = Brand.objects.all()
    context['qs'] = qs
    if request.method == "POST":
        form = BrandFormm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createBrand")
    return render(request, "Rent/CreateBrand.html", context)

@login_required(login_url="Logincheck")
def BrandEdit(request, pk):
    form = Brand.objects.get(id=pk)
    form = BrandFormm(instance=form)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = Brand.objects.get(id=pk)
        form = BrandFormm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createBrand")
    return render(request, "Rent/BrandEdit.html", context)

@login_required(login_url="Logincheck")
def BrandDel(request, pk):
    dele = Brand.objects.get(id=pk)
    dele.delete()
    qs = BrandFormm()
    context = {}
    context['del'] = qs
    qs = Brand.objects.all()
    context['brand'] = qs
    return redirect("createBrand")


def HomeCheck(request):
    return render(request, "Rent/base.html")

@login_required(login_url="Logincheck")
def Carcreate(request):
    form = CarRentFormm()
    context = {}
    context['form'] = form
    qs = Car.objects.all()
    context['cars'] = qs
    if request.method == "POST":
        form = CarRentFormm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Carcreate")
    return render(request, "Rent/Carcreate.html", context)

@login_required(login_url="Logincheck")
def CarEdit(request, pk):
    qs = Car.objects.get(id=pk)
    form = CarRentFormm(instance=qs)
    context = {}
    context['edit'] = form
    if request.method == "POST":
        qs = Car.objects.get(id=pk)
        form = CarRentFormm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "Rent/caredit.html", context)


def DeleteCar(request, pk):
    dele = Brand.objects.get(id=pk)
    dele.delete()
    qs = BrandFormm()
    context = {}
    context['del'] = qs
    qs = Brand.objects.all()
    context['delcar'] = qs
    return redirect("Carcreate")

@login_required(login_url="Logincheck")
def index(request):
    obj = Car.objects.all()
    context = {'view': obj}
    form = SearchForm
    context['search'] = form
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data.get("brand_name")
            items = Car.objects.filter(brand_nme__brand_name=brand)
            context['view'] = items
            return render(request, "Rent/index.html", context)
    return render(request, "Rent/index.html", context)


def RegistraionCreate(request):
    form = RegisterationFm()
    context = {}
    context['register'] = form
    if request.method == "POST":
        form = RegisterationFm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Logincheck")
    return render(request, "Rent/Registrationpage.html", context)


def Logincheck(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ",", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("Logincheck")
    return render(request, "Rent/Loginpage.html")


def OrderCreate(request, pk):
    context = {}
    form = OrderForm(initial={'car_id': pk, "user": request.user})
    context['orderr'] = form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Rent/success.html")
    return render(request, "Rent/usercreation.html", context)


def ViewOrder(request):
    qs = Orders.objects.all()
    context = {'order': qs}
    return render(request, "Rent/vieworder.html", context)

def orderDetails(request, pk):
    qs = Orders.objects.get(id=pk)
    form = OrderUpdatefm(instance=qs)
    context = {'form': form}
    if request.method == "POST":
        form = OrderUpdatefm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworder")
    return render(request, "Rent/orderdetails.html", context)

def Logout(request):
    logout(request)
    return redirect("Logincheck")
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from Rent.forms import SearchForm, RegisterationFm
from Clientapp.forms import OrderUpdatefm, OrderForm
from Rent.models import Car, Orders
from django.contrib.auth.decorators import login_required


@login_required(login_url="LogincheckUser")
def Userindex(request):
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
            return render(request, "Clientapp/userindex.html", context)
    return render(request, "Clientapp/userindex.html", context)


def RegistraionUser(request):
    form = RegisterationFm()
    context = {}
    context['register'] = form
    if request.method == "POST":
        form = RegisterationFm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("LogincheckUser")
    return render(request, "Clientapp/Registrationpage.html", context)


def LogincheckUser(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ",", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("LogincheckUser")
    return render(request, "Clientapp/Loginpage.html")


@login_required(login_url="LogincheckUser")
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


@login_required(login_url="LogincheckUser")
def ViewOrderUser(request):
    qs = Orders.objects.filter(user=request.user)
    context = {'order': qs}
    return render(request, "Clientapp/vieworder.html", context)


@login_required(login_url="LogincheckUser")
def orderDetails(request, pk):
    qs = Orders.objects.get(id=pk)
    form = OrderUpdatefm(instance=qs)
    context = {'form': form}
    if request.method == "POST":
        form = OrderUpdatefm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworder")
    return render(request, "Clientapp/orderdetails.html", context)

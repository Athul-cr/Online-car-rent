from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from Hrapp.forms import RegisterationFm
from Leaveapp.forms import Leavemgmntfm
from Leaveapp.models import Leavemgmnt
from django.contrib.auth.decorators import login_required



def Register(request):
    form = RegisterationFm()
    context = {'form': form}
    if request.method == "POST":
        form = RegisterationFm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Logincheck")
        else:
            context = {}
            context['form'] = form
            return render(request, "Leaveapp/UserRegister.html", context)
            print("valid")
    return render(request, "Leaveapp/UserRegister.html", context)


def Logincheck(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ",", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Userhome")
    return render(request, "Leaveapp/UserLogin.html")


# Create your views here.
@login_required(login_url='Logincheck')
def Userhome(request):
    form = Leavemgmntfm()
    context = {'form': form}
    if request.method == 'POST':
        # leave_Status=request.POST('leave_status')
        obj = Leavemgmnt.objects.all()
        obj.leave_Status = 'pending'
        context['status'] = obj.leave_Status
        print(obj.leave_Status)
        form = Leavemgmntfm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Leaveapp/check.html", context)
    return render(request, "Leaveapp/userhome.html", context)

@login_required(login_url='Logincheck')
def Viewstatus(request, pk):
    obj = Leavemgmnt.objects.get(id=pk)
    status = obj.leave_status
    context = {}
    context['status'] = status
    return render(request, "Leaveapp/Viewstatus.html", context)


def Landinguser(request):
    return render(request, "Leaveapp/Userbase.html")

@login_required(login_url='Logincheck')
def IndexUser(request):
    return render(request, "Leaveapp/index.html")

def LogOut(request):
    logout(request)
    return redirect("Logincheck")

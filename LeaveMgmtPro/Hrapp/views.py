from django.shortcuts import render, redirect
from Hrapp.forms import RegisterationFm, HrUserFm, LeaveConfirmfm
from django.contrib.auth import authenticate, login, logout
from Hrapp.models import HrUserMod
from Leaveapp.models import Leavemgmnt
from django.contrib.auth.decorators import login_required
from Leaveapp.forms import Leavemgmntfm


# Create your views here.


def RegistraionCreate(request):
    form = RegisterationFm()
    context = {}
    context['register'] = form
    if request.method == "POST":
        form = RegisterationFm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Loginhr")
    return render(request, "Hrapp/Registration.html", context)


def Loginhr(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ",", password)
        if (username == "hr") & (password == "hr123"):
            return render(request, "Hrapp/Hrhome.html")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "Hrapp/Hrhome.html")
        else:
            return redirect("Loginhr")
    return render(request, "Hrapp/Login.html")

@login_required(login_url='Loginhr')
def Createuser(request):
    form = HrUserFm()
    context = {'form': form}
    qs = HrUserMod.objects.all()
    context['create'] = qs
    if request.method == 'POST':
        form = HrUserFm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Createuser")
    return render(request, "Hrapp/Hrhome.html", context)

@login_required(login_url='Loginhr')
def EditUser(request, pk):
    obj = HrUserMod.objects.get(id=pk)
    form = HrUserFm(instance=obj)
    context = {'edit': form}
    if request.method == "POST":
        print("inside post")
        obj = HrUserMod.objects.get(id=pk)
        form = HrUserFm(instance=obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            print("inside edit")
            form.save()
            return redirect("Createuser")
        else:
            form = HrUserFm(request.POST)
            context = {}
            context['edit'] = form
            return render(request, "Hrapp/Edituser.html", context)
    return render(request, "Hrapp/Edituser.html", context)

@login_required(login_url='Loginhr')
def DeletePro(request, pk):
    dele = HrUserMod.objects.get(id=pk)
    dele.delete()
    form = HrUserFm()
    context = {'del': form}
    qs = HrUserMod.objects.all()
    context['Prodel'] = qs
    return redirect("Createuser")

@login_required(login_url='Loginhr')
def Hrhome(request, pk):
    qs = Leavemgmnt.objects.all()
    context = {'Edit': qs}
    return render(request, "Hrapp/status.html", context)

@login_required(login_url='Loginhr')
def Leaveconfirm(request, pk):
    qs = Leavemgmnt.objects.get(id=pk)
    form = LeaveConfirmfm(instance=qs)
    context = {}
    context['form'] = form
    if request.method == "POST":
        qs = Leavemgmnt.objects.get(id=pk)
        form = LeaveConfirmfm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Hrapp/statuscheck.html")

    return render(request, "Hrapp/Editstatus.html", context)

@login_required(login_url='Loginhr')
def DeleteStatus(request, pk):
    dele = Leavemgmnt.objects.get(id=pk)
    dele.delete()
    form = LeaveConfirmfm()
    context = {'del': form}
    qs = Leavemgmnt.objects.all()
    context['Prodel'] = qs
    return redirect("Createuser")

@login_required(login_url='Loginhr')
def Landing(request):
    return render(request, "Hrapp/base.html")

def LogOuthr(request):
    logout(request)
    return redirect("Loginhr")

# qs = models.objects.get(id=pk)
# qs.active_status=1
# qs.save()

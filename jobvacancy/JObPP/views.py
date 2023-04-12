
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from JObPP.models import Company,City


# Create your views here.
def login_fun(request):
    return render(request, "loing.html",{'data':''})


def logdata_fun(request):
    UserName = request.POST['txtUserName']
    Password = request.POST['txtPassword']
    user1 = authenticate(username = UserName,password = Password)

    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request, "loing.html",{'data':'USer is not a superuser'})
    else:
        return render(request, "loing.html",{'data':'Enter proper user name and password'})


def home_fun(request):
    return render(request,'home.html')


def reg_fun(request):
    return render(request, "register.html", {'data': ''})


def regdata_fun(request):
    UserName = request.POST['txtUserName']
    Email = request.POST['txtEmail']
    Password = request.POST['txtPassword']

    if User.objects.filter(Q(username=UserName) | Q(email=Email)).exists():
        return render(request, "register.html", {'data': 'USerName and Email is already exists'})

    else:
        u1 = User.objects.create_superuser(username=UserName, email=Email, password=Password)
        u1.save()
        return redirect('log')


def addjob_fun(request):
      city = City.objects.all()
      return render(request,'addjob.html',{'city_data':city})


def readdata_fun(request):
    c1 = Company()
    c1.Name = request.POST['txtName']
    c1.jobdescription = request.POST['txtjobdescription']
    c1.City = City.objects.get(city_name = request.POST['ddlCity'])
    c1.vacancy = request.POST['txtVacancy']
    c1.applied = request.POST['txtApplied']
    c1.save()
    return redirect('add')


def display_fun(request):
    c1 = Company.objects.all()
    return render(request, 'display.html', {'net': c1})




def apply_fun(request,id):
    c1 = Company.objects.get(id=id)
    city = City.objects.all()
    if request.method == 'POST':
        c1.Name = request.POST['txtName']
        c1.Phno = request.POST['txtPhno']
        c1.Email = request.POST['txtEmail']
        c1.City =  City.objects.get(city_name  = request.POST['ddlCity'])
        c1.save()
        return redirect('applied')

    return render(request,'apply.html',{'net':c1,'City_Data':city})


def applied_fun(request):
    return render(request, 'applied.html')

def log_out_fun(request):
    logout(request)
    return redirect('log')

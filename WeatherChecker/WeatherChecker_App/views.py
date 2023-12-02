from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django. contrib import messages
from django.contrib import auth
from WeatherChecker_App import urls
from django.urls import include
import requests
from WeatherChecker_App.models import Users


# Create your views here.

def index(request,**kwargs):
    return render(request,'home.html')

def signup(request, **kwargs):
    return render(request,'signup.html')

def login(request, **kwargs):
    return render(request,'login.html')

def signupSubmit(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email1=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm-password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        print(User.objects.filter(email=email1).exists())
        if password==cpassword:
            print("aagya re baba ..................................")
            if User.objects.filter(email=email1).exists():
                print('email')
                messages.info(request,'Email Already Registered')
                return render(request,'signup.html')
            elif Users.objects.filter(username=username).exists():
                print('name')
                messages.info(request,'Username Already Registered')
                return render(request,'signup.html')
            else:
                print('done')
                user_obj=User(username=username, password=password, email=email1, first_name=firstname, last_name=lastname)
                user_obj.save()
                context={'val':True}
                return render(request,'login.html',context)
        else:
            print('pwd')
            messages.info(request,"Password don't match")
            return render(request,'signup.html')
   

def loginSubmit(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Login Info..')
            return redirect('login.html')
    return render(request,'login.html')
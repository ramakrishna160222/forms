from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password2)
                user.save()

        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'user not active')
                return redirect('login')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
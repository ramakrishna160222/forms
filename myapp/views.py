from django.shortcuts import render,redirect
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def insert(request):
    if request.method=="POST":
        stu=StudentForm(request.POST,request.FILES)
        if stu.is_valid():
            name=stu.cleaned_data['name']
            branch=stu.cleaned_data['branch']
            profile_pic=stu.cleaned_data['profile_pic']
            stu.save()
            return redirect('/')

    else:
        stu=StudentForm()
    return render(request,'insert.html',{'form':stu})

def show(request):
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})




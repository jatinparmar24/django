from django.shortcuts import render
from .models import *


# Create your views here.


def landing(request):
    return render(request,'landing.html')

# def index(request):
#     return render(request,'index.html')

def first(request):
    data=Student.objects.all()[0:5]
    return render(request,'landing.html',{'data':data})

def last(request):
    data=Student.objects.order_by('-stu_name')[:5] 
    return render(request,'landing.html',{'data':data})

def asc(request):
    data=Student.objects.order_by('stu_name')
    return render(request,'landing.html',{'data':data})

def desc(request):
    data=Student.objects.order_by('-stu_name')
    return render(request,'landing.html',{'data':data})

def all(request):
    data=Student.objects.all()
    return render(request,'landing.html',{'data':data})
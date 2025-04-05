from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app3(request):
    return HttpResponse('<h1 style=color:red>The Box </h1>')
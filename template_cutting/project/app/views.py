from django.shortcuts import render

# Create your views here.

def home(request):
    return render('request','loading.html')

def About(request):
    return render(request,'About.html')
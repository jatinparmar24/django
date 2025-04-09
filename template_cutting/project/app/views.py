from django.shortcuts import render

# Create your views here.

def home(request):
    return render('request','loading.html')

def About(request):
    return render(request,'About.html')

def terms(request):
    return render(request,'terms.html')

def services(request):
    return render(request,'services.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def register(request):
    print("register page")
    print(request.method)
    print(request.POST)
    print(request.FILES)
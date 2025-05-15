from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html')


def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def sett(request):
    data=render(request,'login.html')
    data.set_cookie('name',request.POST.get('name'))
    data.set_cookie('email',request.POST.get('email'))
    data.set_cookie('phone',request.POST.get('phone '))
    return data


def get(request):
    if request.method=='POST':
        name=request.COOKIES['name']
        email=request.COOKIES['email']

        ename=request.POST.get('name')
        eemail=request.POST.get('email')

        if ename==name and email==eemail:
            return render(request,'dashboard.html')
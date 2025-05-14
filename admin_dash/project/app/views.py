from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')


def admindata(request):
    return render(request,'login.html')


def admin_login(request):
    if request.method=='POST':
        email="admin@gmail.com"
        password="admin@123"

        e=request.POST.get('email')
        p=request.POST.get('password')

        if e==email and p==password:
            request.session['logged_in'] = True
            return render(request,'admindata.html')

        else:
            messages="Please Enter Valid Email"
            return render(request,'login.html',{'messages':messages})


def admin_logout(request):
    request.session.flush()
    return render(request,'home.html')

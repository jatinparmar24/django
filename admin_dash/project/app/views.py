from django.shortcuts import render,redirect
from .models import Employee 



# Create your views here.

def home(request):
    return render(request,'home.html')


def admindata(request):
    return render(request,'login.html')

def adminpage(request):
    return render(request,'admindata.html')


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



from django.contrib import messages
from .models import Employee

def add_emp(request):
    show_form = request.GET.get('show_form') == 'true'

    if request.method == 'POST':
        emp_name = request.POST.get('name')
        emp_contact = request.POST.get('phone')
        emp_dob = request.POST.get('dob')
        emp_email = request.POST.get('email')
        emp_pass = request.POST.get('password')
        emp_image = request.FILES.get('profile-pic')

     
        Employee.objects.create(
            emp_name=emp_name,
            emp_contact=emp_contact,
            emp_dob=emp_dob,
            emp_email=emp_email,
            emp_pass=emp_pass,
            emp_image=emp_image
        )

        
        return redirect('adminpage')

    return render(request, 'admindata.html', {'show_form': show_form})

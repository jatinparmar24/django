from django.shortcuts import render,redirect
from .models import Employee 



# Create your views here.

def home(request):
    return render(request,'home.html')


# navbar admin page
def admindata(request):
    return render(request,'login.html')


# Admin data view
def admindata1(request):
    is_admin = request.session.get('is_admin', False)
    show_form = request.GET.get('show_form') == '1'  # True if URL contains ?show_form=1
    return render(request, 'admindata.html', {'data': is_admin, 'show_form': show_form})

# Home view
def home1(request):
    is_admin = request.session.get('is_admin', False)
    return render(request, 'home.html', {'data': is_admin})

def logout(request):
    request.session.flush()
    return redirect('home')





# render to login page
def userlogin(request):
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

from django.shortcuts import render, redirect

# Admin login view
def admin_login(request):
    if request.method == 'POST':
        email = "admin@gmail.com"
        password = "ad"
        e = request.POST.get('email')
        p = request.POST.get('password')

        if e == email and p == password:
            request.session['is_admin'] = True 
            return redirect('admindata1')       
        else:
            messages = "Please Enter Valid Email"
            return render(request, 'login.html', {'messages': messages})
    return render(request, 'login.html')



def logout(request):
    request.session.flush() 
    return redirect('home')

def add_employe(request):
    return render(request,'admindata.html')



def add_emp(request):
    if not request.session.get('is_admin'):
        # Redirect to login if not admin
        return redirect('admin_login')

    if request.method == 'POST':
        emp_name    = request.POST.get('name')
        emp_contact = request.POST.get('phone')
        emp_dob     = request.POST.get('dob')
        emp_email   = request.POST.get('email')
        emp_pass    = request.POST.get('password')
        emp_image   = request.FILES.get('profile-pic')

        Employee.objects.create(
            emp_name=emp_name,
            emp_contact=emp_contact,
            emp_dob=emp_dob,
            emp_email=emp_email,
            emp_pass=emp_pass,
            emp_image=emp_image
        )
        return redirect('admindata1')  

    return render(request, 'admindata.html', {'data': True, 'show_form': True})



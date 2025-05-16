from django.shortcuts import render,redirect
from .models import Employee 
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request,'home.html')


# navbar admin page
def admindata(request):
    return render(request,'login.html')


# Admin data view
def admindata1(request):
    is_admin = request.session.get('is_admin', False)
    show_form = request.GET.get('show_form') == '1' 
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


# Admin login view
def admin_login(request):
    if request.method == 'POST':
        admin_email = "admin@gmail.com"
        admin_password = "ad"

        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Both fields are required.")
            return render(request, 'login.html')

        # Admin Login
        if email == admin_email and password == admin_password:
            request.session['is_admin'] = True
            return redirect('admindata1')

        # User Login
        try:
            employee = Employee.objects.get(emp_email=email, emp_pass=password)
            request.session['user_email'] = employee.emp_email
            request.session['user_id'] = employee.id  # Add this line
            return redirect('user_info')
        except Employee.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')



def logout(request):
    request.session.flush() 
    return redirect('home')



def add_emp(request):
    if not request.session.get('is_admin'):
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


def show_all_emp(request):
    emp_data=Employee.objects.all()
    return render(request,'admindata.html',{'emp_data':emp_data,'show_all': True})

def userdetail(request):
    return render(request,'userdetail.html')


def user_info(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')

    show_table = request.GET.get('show_table') == '1'

    user_data = None
    if show_table:
        user_data = Employee.objects.filter(emp_email=email)

    return render(request, 'userdetail.html', {
        'user_data': user_data,
        'show_table': show_table,
    })


def edit_emp(request, id):
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return redirect('show_employees')

    if request.method == 'POST':
        emp.emp_name = request.POST.get('name')
        emp.emp_contact = request.POST.get('contact')
        emp.emp_dob = request.POST.get('dob')
        emp.emp_email = request.POST.get('email')
        emp.emp_pass = request.POST.get('pass')
        
        if request.FILES.get('image'):
            emp.emp_image = request.FILES['image']
        
        emp.save()
        # Instead of redirect, continue to show form with updated data

    emp_data = Employee.objects.all()
    return render(request, 'admindata.html', {
        'show_all': True,
        'emp_data': emp_data,
        'edit_employee': emp
    })

def delete_employee(request, id):
    try:
        emp = Employee.objects.get(id=id)
        emp.delete()
    except Employee.DoesNotExist:
        pass
    return redirect('admindata1')
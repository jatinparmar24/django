from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Employee,NewEntry



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


def userdetail(request):
    user_email = request.session.get('user_email')
    emp_data = None
    resumes = None

    if user_email:
        try:
            # Get employee info
            emp_data = Employee.objects.filter(emp_email=user_email)

            # Get resumes related to this user, matching contact or email
            resumes = NewEntry.objects.filter(info_contact__in=[emp.emp_contact for emp in emp_data])
        except Employee.DoesNotExist:
            emp_data = None
            resumes = None

    return render(request, 'userdetail.html', {
        'emp_data': emp_data,
        'resumes': resumes,
        'view_user': True,     # to show employee info table as before
        'show_resumes': True   # flag to show resumes with admin opinions
    })



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
            request.session['user_id'] = employee.id  
            request.session['employee_id'] = employee.id
            return redirect('userdetail')
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
        emp_depart  = request.POST.get('emp_depart') 

        Employee.objects.create(
            emp_name=emp_name,
            emp_contact=emp_contact,
            emp_dob=emp_dob,
            emp_email=emp_email,
            emp_pass=emp_pass,
            emp_image=emp_image,
            emp_depart=emp_depart  
        )
        return redirect('admindata1')

    return render(request, 'admindata.html', {'data': True, 'show_form': True})



def show_all_emp(request):
    emp_data=Employee.objects.all()
    return render(request,'admindata.html',{'emp_data':emp_data,'show_all': True})



def edit_emp(request,id):
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

    

def view_user(request):
    user_id = request.session.get('user_id')  
    if user_id:
        emp_data = Employee.objects.filter(id=user_id)
        return render(request, 'userdetail.html', {
            'emp_data': emp_data,
            'view_user': True,   # flag to show the table
        })
    else:
        return redirect('login')

def find_user(request):
    if request.method == 'POST':
        name     = request.POST.get('name')
        contact  = request.POST.get('contact')
        dob      = request.POST.get('dob')
        resume   = request.POST.get('resume')
        image    = request.FILES.get('profile-pic')

        NewEntry.objects.create(
            info_name=name,
            info_contact=contact,
            info_dob=dob,
            info_resume=resume,
            info_image=image
        )

        messages.success(request, "Your information has been submitted.")
        return redirect('userdetail')

    return render(request, 'userdetail.html', {'find_user': True})


# for admin to show that resume


def show_resume(request):
    show_resumes = request.GET.get('show_resumes', 'false').lower() == 'true'
    resumes = []

    if show_resumes:
        resumes = NewEntry.objects.all()  # Or filter by user/session if needed

    return render(request, 'userdetail.html', {
        'show_resumes': show_resumes,
        'resumes': resumes,
    })


def admin_resumes(request):
    if request.method == 'POST':
        resume_id = request.POST.get('resume_id')
        opinion = request.POST.get('admin_opinion', '')# can use .strip() to remove unwanted extra space

        if resume_id and opinion is not None:
            try:
                resume = NewEntry.objects.get(id=resume_id)
                resume.admin_opinion = opinion
                resume.save()
            except NewEntry.DoesNotExist:
                pass  

        return redirect('admin_resumes')

    resumes = NewEntry.objects.all()

    return render(request, 'admindata.html', {
        'admin_resumes': True,
        'resumes': resumes,
    })


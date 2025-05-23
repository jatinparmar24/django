from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Employee,NewEntry
from django.db.models import Q
from django.core.paginator import Paginator




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
        admin_email = "admin@email.com"
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

    show_form = False

    if request.method == 'POST':
        if 'show_form' in request.POST:
            show_form = request.POST.get('show_form') == '1'
        else:
            emp_name    = request.POST.get('name')
            emp_contact = request.POST.get('phone')
            emp_dob     = request.POST.get('dob')
            emp_email   = request.POST.get('email')
            emp_pass    = request.POST.get('password')
            emp_image   = request.FILES.get('profile-pic')
            emp_depart  = request.POST.get('emp_depart')

            # Check if email or password already exists
            email_exists = Employee.objects.filter(emp_email=emp_email).exists()
            password_exists = Employee.objects.filter(emp_pass=emp_pass).exists()
            
            if email_exists:
                messages.error(request, 'Email already exists. Please use a different email.')
                show_form = True  # to show form again with the error
            elif password_exists:
                messages.error(request, 'Password already exists. Please use a different password.')
                show_form = True
            else:
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

    return render(request, 'admindata.html', {
        'data': True,
        'show_form': show_form
    })


def show_all_emp(request):
    emp_list = Employee.objects.all()
    paginator = Paginator(emp_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    start_index = page_obj.start_index()

    return render(request, 'admindata.html', {
        'show_all': True,
        'emp_data': page_obj,          
        'start_index': start_index,      
        'edit_employee': None            
    })

def edit_emp(request, emp_id):
    try:
        emp = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('show_all_emp')  # make sure redirect URL name is correct

    if request.method == 'POST':
        # update fields...
        emp.emp_name = request.POST.get('name')
        emp.emp_contact = request.POST.get('contact')
        emp.emp_dob = request.POST.get('dob')
        emp.emp_email = request.POST.get('email')
        emp.emp_pass = request.POST.get('pass')
        
        if request.FILES.get('image'):
            emp.emp_image = request.FILES['image']
        
        emp.save()

    emp_list = Employee.objects.all()
    paginator = Paginator(emp_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    start_index = page_obj.start_index()

    return render(request, 'admindata.html', {
        'show_all': True,
        'emp_data': page_obj,
        'edit_employee': emp,
        'start_index': start_index,
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
    show_resumes = False
    resumes = []

    if request.method == 'POST':
        show_resumes = request.POST.get('show_resumes', 'false').lower() == 'true'
    else:
        show_resumes = request.GET.get('show_resumes', 'false').lower() == 'true'

    if show_resumes:
        all_resumes = NewEntry.objects.all().order_by('id')  
        paginator = Paginator(all_resumes, 5)
        page_number = request.GET.get('page')
        resumes = paginator.get_page(page_number)

    return render(request, 'userdetail.html', {
        'show_resumes': show_resumes,
        'resumes': resumes,
    })


def admin_resumes(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'toggle_show':
            # Show the page with both tables paginated (like GET)
            resumes_all = NewEntry.objects.all()

            submitted_page_number = request.GET.get('submitted_page')
            manage_page_number = request.GET.get('manage_page')

            submitted_paginator = Paginator(resumes_all, 5)
            manage_paginator = Paginator(resumes_all, 5)

            submitted_page = submitted_paginator.get_page(submitted_page_number)
            manage_page = manage_paginator.get_page(manage_page_number)

            return render(request, 'admindata.html', {
                'submitted_page': submitted_page,
                'manage_page': manage_page,
                'admin_resumes': True,   # so your template shows tables
            })

        # Else handle opinion update POST
        resume_id = request.POST.get('resume_id')
        opinion = request.POST.get('admin_opinion', '')

        if resume_id and opinion is not None:
            try:
                resume = NewEntry.objects.get(id=resume_id)
                resume.admin_opinion = opinion
                resume.save()
            except NewEntry.DoesNotExist:
                pass  

        return redirect('admin_resumes')

    # GET request: normal page load
    resumes_all = NewEntry.objects.all()

    submitted_page_number = request.GET.get('submitted_page')
    manage_page_number = request.GET.get('manage_page')

    submitted_paginator = Paginator(resumes_all, 5)
    manage_paginator = Paginator(resumes_all, 5)

    submitted_page = submitted_paginator.get_page(submitted_page_number)
    manage_page = manage_paginator.get_page(manage_page_number)

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'admin_resumes': True,   # important for template to display tables
    })


# to search


def search_emp(request):
    pk = request.POST.get('search')
    all_data = Employee.objects.filter(
        Q(emp_name__icontains=pk) |
        Q(emp_contact__icontains=pk) |
        Q(emp_dob__icontains=pk) |
        Q(emp_email__icontains=pk) |
        Q(emp_depart__icontains=pk)
    )

    paginator = Paginator(all_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    start_index = page_obj.start_index()

    return render(request, 'admindata.html', {
        'emp_data': page_obj,
        'start_index': start_index,
        'show_all': True
    })


def search_with_detail(request):
    name = request.POST.get('name', '').strip()
    contact = request.POST.get('contact', '').strip()
    dob = request.POST.get('dob', '').strip()
    email = request.POST.get('email', '').strip()
    depart = request.POST.get('depart', '').strip()

    query = Q()
    if name:
        query |= Q(emp_name__icontains=name)
    if contact:
        query |= Q(emp_contact__icontains=contact)
    if dob:
        query |= Q(emp_dob__icontains=dob)
    if email:
        query |= Q(emp_email__icontains=email)
    if depart:
        query |= Q(emp_depart__icontains=depart)

    filtered_data = Employee.objects.filter(query) if query else Employee.objects.none()

    paginator = Paginator(filtered_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    start_index = page_obj.start_index()

    return render(request, 'admindata.html', {
        'emp_data': page_obj,
        'start_index': start_index,
        'show_all': True
    })


# for ordering data
def orderby_name(request):
    emp_list = Employee.objects.all().order_by('emp_name')  
    paginator = Paginator(emp_list, 5)  
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    start_index = (page_obj.number - 1) * paginator.per_page + 1

    return render(request, 'admindata.html', {
        'emp_data': page_obj,
        'page_obj': page_obj,
        'start_index': start_index
    })

def name_in_desc(request):
    emp_list = Employee.objects.all().order_by('-emp_name')  
    paginator = Paginator(emp_list, 5)  
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    start_index = (page_obj.number - 1) * paginator.per_page + 1

    return render(request, 'admindata.html', {
        'emp_data': page_obj,
        'page_obj': page_obj,
        'start_index': start_index
    })


def orderby_name_admin(request):
    submitted_list = NewEntry.objects.all().order_by('info_name')
    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index_submitted = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    
    manage_list = NewEntry.objects.all()  
    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index_submitted,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })


def orderby_name_admin_desc(request):
    submitted_list = NewEntry.objects.all().order_by('-info_name')
    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index_submitted = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    manage_list = NewEntry.objects.all()
    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index_submitted,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })



def orderby_name_adminM(request):
    submitted_list = NewEntry.objects.all()
    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index_submitted = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    manage_list = NewEntry.objects.all().order_by('info_name')
    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index_submitted,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })



def orderby_name_admin_descM(request):
    submitted_list = NewEntry.objects.all()
    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index_submitted = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    
    manage_list = NewEntry.objects.all().order_by('-info_name')
    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index_submitted,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })


# search for resume and manage resume in admin

def search_detailR(request):
    pk = request.POST.get('search', '').strip()
    submitted_list = NewEntry.objects.filter(
        Q(info_name__icontains=pk) |
        Q(info_contact__icontains=pk) |
        Q(info_dob__icontains=pk)
    )

    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    manage_list = NewEntry.objects.all()
    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })


def search_detailM(request):
    pk = request.POST.get('search', '').strip()
    manage_list = NewEntry.objects.filter(
        Q(info_name__icontains=pk) |
        Q(info_contact__icontains=pk) |
        Q(info_dob__icontains=pk)
    )

    manage_paginator = Paginator(manage_list, 5)
    manage_page_number = request.GET.get('manage_page')
    manage_page = manage_paginator.get_page(manage_page_number)
    start_index_manage = (manage_page.number - 1) * manage_paginator.per_page + 1

    submitted_list = NewEntry.objects.all()
    submitted_paginator = Paginator(submitted_list, 5)
    submitted_page_number = request.GET.get('page')
    submitted_page = submitted_paginator.get_page(submitted_page_number)
    start_index = (submitted_page.number - 1) * submitted_paginator.per_page + 1

    return render(request, 'admindata.html', {
        'submitted_page': submitted_page,
        'manage_page': manage_page,
        'start_index': start_index,
        'start_index_manage': start_index_manage,
        'admin_resumes': True,
    })


# search for resume and manage resume in admin

# for userdashboard
def asc_for_aResume(request):
    resume_list = NewEntry.objects.all().order_by('info_name')
    paginator = Paginator(resume_list, 5)
    page_number = request.GET.get('page')
    resumes = paginator.get_page(page_number)
    return render(request, 'userdetail.html', {
        'resumes': resumes,
        'show_resumes': True,
    })

def desc_for_aResume(request):
    resume_list = NewEntry.objects.all().order_by('-info_name')
    paginator = Paginator(resume_list, 5)
    page_number = request.GET.get('page')
    resumes = paginator.get_page(page_number)
    return render(request, 'userdetail.html', {
        'resumes': resumes,
        'show_resumes': True,
    })

def search_aResume(request):
    if request.method == 'POST':
        query = request.POST.get('search', '')
        resume_list = NewEntry.objects.filter(
            Q(info_name__icontains=query) |
            Q(info_contact__icontains=query) |
            Q(info_dob__icontains=query)
        )
    else:
        resume_list = NewEntry.objects.all()

    paginator = Paginator(resume_list, 5)
    page_number = request.GET.get('page')
    resumes = paginator.get_page(page_number)
    return render(request, 'userdetail.html', {
        'resumes': resumes,
        'show_resumes': True,
    })

# for userdashboard
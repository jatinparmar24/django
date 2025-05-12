from django.shortcuts import render,redirect
from .models import Students,Items


# Create your views here.

def home(request):
    return render(request,'home.html')


def home1(request, pk):
    userdata = Students.objects.get(id=pk)
    userdata = {
        "id": userdata.id,
        "name": userdata.stuname,
        "email": userdata.stuemial,
        "des": userdata.studetails,
        "phone": userdata.stuphone,
        "dob": userdata.studob,
        "sub": userdata.stuedu,
        "gender": userdata.stugender,
        "image": userdata.stuimage,
        "resume": userdata.sturesume,
        "pass": userdata.stupass,
    }
    return render(request, 'home.html', {'userdata': userdata})



def about(request):
    return render(request,'about.html')


def about1(request, pk):
    userdata = Students.objects.get(id=pk)
    userdata = {
        "id": userdata.id,
        "name": userdata.stuname,
        "email": userdata.stuemial,
        "des": userdata.studetails,
        "phone": userdata.stuphone,
        "dob": userdata.studob,
        "sub": userdata.stuedu,
        "gender": userdata.stugender,
        "image": userdata.stuimage,
        "resume": userdata.sturesume,
        "pass": userdata.stupass,
    }
    return render(request, 'about.html', {'userdata': userdata})



def service(request):
    return render(request,'service.html')


def service1(request, pk):
    userdata = Students.objects.get(id=pk)
    userdata = {
        "id": userdata.id,
        "name": userdata.stuname,
        "email": userdata.stuemial,
        "des": userdata.studetails,
        "phone": userdata.stuphone,
        "dob": userdata.studob,
        "sub": userdata.stuedu,
        "gender": userdata.stugender,
        "image": userdata.stuimage,
        "resume": userdata.sturesume,
        "pass": userdata.stupass,
    }
    return render(request, 'service.html', {'userdata': userdata})


def alldata(request):
    users = Students.objects.all()
    return render(request, 'alldata.html', {'users': users})

def alldata1(request,pk):
    users = Students.objects.all()
    student = Students.objects.get(id=pk)

    context = {
        "id": student.id,
        "name": student.stuname,
        "email": student.stuemial,
        "des": student.studetails,
        "phone": student.stuphone,
        "dob": student.studob,
        "sub": student.stuedu,
        "gender": student.stugender,
        "image": student.stuimage,
        "resume": student.sturesume,
        "pass": student.stupass,
    }
    return render(request, 'alldata.html', {'users': users, 'userdata': context})


def dashboard(request, pk):
    student = Students.objects.get(id=pk)
    context = {
        "id": student.id,
        "name": student.stuname,
        "email": student.stuemial,
        "des": student.studetails,
        "phone": student.stuphone,
        "dob": student.studob,
        "sub": student.stuedu,
        "gender": student.stugender,
        "image": student.stuimage,
        "resume": student.sturesume,
        "pass": student.stupass,
    }
    return render(request, 'dashboard.html', {'userdata': context})





def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html',{'key':key})




def logindata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pasw = request.POST.get('password')
        user = Students.objects.filter(stuemial=email).first()

        if user: 
            if pasw == user.stupass:
                return redirect('dashboard', pk=user.id)
            else:

                msg = 'Email and Password Not Matched'
        else:
            msg = "Email Not Registered"

        return render(request, 'login.html', {'msg': msg, 'email': email})

    return render(request, 'login.html')







def register(request):
    print("register page")
    print(request.method)
    print(request.POST)
    print(request.FILES)

    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    profilepic=request.FILES.get('profile-pic')
    resume=request.FILES.get('resume')
    # print(username)
    # print(email)
    # print(detail)
    # print(phone)
    # print(dob)
    # print(subscribe)
    # print(gender)
    # print(password)
    # print(cpassword)
    # print(profilepic)
    # print(resume)
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,resume)

    user=Students.objects.filter(stuemial=email)
    if user:
        msg="Email Already Exixted "
        return render(request,'registration.html',{'key':msg})

    else:
        if password==cpassword:
            Students.objects.create(stuname=username,stuemial=email,studetails=detail,stuphone=phone,studob=dob,stuedu=subscribe,stugender=gender,stuimage=profilepic,sturesume=resume,stupass=password)
            msg="Registration Successfull"
            return render(request,'login.html',{'key':msg})

        else:
            msg="Check Password And Confirm Password again"
            return render(request,'registration.html',{'key':msg})



def dash(request):
    return render(request,'login.html')


def first(request,pk):
    print(pk)
    userdata=Students.objects.get(id=pk)
    key = Items.objects.all()[:5]  
    return render(request, 'dashboard.html', {'userdata':userdata,'key':key})

def last(request,pk):
    userdata=Students.objects.get(id=pk)
    key = Items.objects.order_by('-id')[:5] 
    return render(request, 'dashboard.html', {'userdata':userdata,'key':key})

def asc(request,pk):
    userdata=Students.objects.get(id=pk)
    key = Items.objects.order_by('item')  
    return render(request, 'dashboard.html', {'userdata':userdata,'key':key})

def desc(request,pk):
    userdata=Students.objects.get(id=pk)
    key = Items.objects.order_by('-item')
    return render(request, 'dashboard.html', {'userdata':userdata,'key':key})

def alld(request,pk):
    userdata=Students.objects.get(id=pk)
    key = Items.objects.all() 
    return render(request, 'dashboard.html', {'userdata':userdata,'key':key})


def edit(request,pk1,pk2):
    userdata = Students.objects.get(id=pk1)
    userdata = {
        "id": userdata.id,
        "name": userdata.stuname,
        "email": userdata.stuemial,
        "des": userdata.studetails,
        "phone": userdata.stuphone,
        "dob": userdata.studob,
        "sub": userdata.stuedu,
        "gender": userdata.stugender,
        "image": userdata.stuimage,
        "resume": userdata.sturesume,
        "pass": userdata.stupass,
    }

    edit_data=Items.objects.get(id=pk2)
    return render(request, 'dashboard.html', {'userdata': userdata,'edit_data':edit_data})
   


def edit_data(request, pk1, pk2):
    if request.method == 'POST':
        edit = Items.objects.get(id=pk2)
        shop_id = request.POST.get('shop')

        edit.name = request.POST.get('item')
        
        edit.quantity = request.POST.get('quantity')
        edit.color = request.POST.get('color')
        edit.save()

        userdata = Students.objects.get(id=pk1)
        userdata = {
            "id": userdata.id,
            "name": userdata.stuname,
            "email": userdata.stuemial,
            "des": userdata.studetails,
            "phone": userdata.stuphone,
            "dob": userdata.studob,
            "sub": userdata.stuedu,
            "gender": userdata.stugender,
            "image": userdata.stuimage,
            "resume": userdata.sturesume,
            "pass": userdata.stupass,
        }

        return render(request, 'dashboard.html', {'userdata': userdata})



        

# def delete(request,pk1,pk2):
#     print(pk1)
#     print(pk2)
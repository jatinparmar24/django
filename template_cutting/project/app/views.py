from django.shortcuts import render
from .models import Students

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



            
       


   
    # Students.objects.create(stuname=username,stuemial=email,studetails=detail,stuphone=phone,studob=dob,stuedu=subscribe,stugender=gender,stuimage=profilepic,sturesume=resume,stupass=password)
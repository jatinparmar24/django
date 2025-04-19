from django.shortcuts import render
from .models import Students

# Create your views here.

def home(request):
    return render(request,'loading.html')

def index1(request,pk):
    userdata=Students.objects.get(id=pk)
    userdata={
                    "id":userdata.id,
                    "name":userdata.stuname,
                    "email":userdata.stuemial,
                    "des":userdata.studetails,
                    "phone":userdata.stuphone,
                    "dob":userdata.studob,
                    "sub":userdata.stuedu,
                    "gender":userdata.stugender,
                    "image":userdata.stuimage,
                    "resume":userdata.sturesume,
                    "pass":userdata.stupass,
                }
    return render(request,'loading.html',{'userdata': userdata})
    


def about(request):
     return render(request,'about.html')


def about1(request,pk):
    userdata=Students.objects.get(id=pk)
    userdata={
                    "id":userdata.id,
                    "name":userdata.stuname,
                    "email":userdata.stuemial,
                    "des":userdata.studetails,
                    "phone":userdata.stuphone,
                    "dob":userdata.studob,
                    "sub":userdata.stuedu,
                    "gender":userdata.stugender,
                    "image":userdata.stuimage,
                    "resume":userdata.sturesume,
                    "pass":userdata.stupass,
                }
    return render(request,'about.html',{'userdata': userdata})


def terms(request):
    return render(request,'terms.html')

def terms1(request,pk):
    userdata=Students.objects.get(id=pk)
    userdata={
                    "id":userdata.id,
                    "name":userdata.stuname,
                    "email":userdata.stuemial,
                    "des":userdata.studetails,
                    "phone":userdata.stuphone,
                    "dob":userdata.studob,
                    "sub":userdata.stuedu,
                    "gender":userdata.stugender,
                    "image":userdata.stuimage,
                    "resume":userdata.sturesume,
                    "pass":userdata.stupass,
                }
    return render(request,'terms.html',{'userdata': userdata})

def services(request):
    return render(request,'services.html')

def services1(request,pk):
    userdata=Students.objects.get(id=pk)
    userdata={
                    "id":userdata.id,
                    "name":userdata.stuname,
                    "email":userdata.stuemial,
                    "des":userdata.studetails,
                    "phone":userdata.stuphone,
                    "dob":userdata.studob,
                    "sub":userdata.stuedu,
                    "gender":userdata.stugender,
                    "image":userdata.stuimage,
                    "resume":userdata.sturesume,
                    "pass":userdata.stupass,
                }
    return render(request,'services.html',{'userdata': userdata})

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pasw=request.POST.get('password')
        user=Students.objects.filter(stuemial=email)
        if user:
            userdata=Students.objects.get(stuemial=email)
            print(userdata.stuname)
            print(userdata.stuemial)
            pass1=userdata.stupass
            if pasw==pass1:
                msg='Welcome To DashBoard'
                userdata={
                    "id":userdata.id,
                    "name":userdata.stuname,
                    "email":userdata.stuemial,
                    "des":userdata.studetails,
                    "phone":userdata.stuphone,
                    "dob":userdata.studob,
                    "sub":userdata.stuedu,
                    "gender":userdata.stugender,
                    "image":userdata.stuimage,
                    "resume":userdata.sturesume,
                    "pass":userdata.stupass,
                }
                return render(request,'dashboard.html',{'userdata':userdata})

            else:
                msg='Email And Password Not Matched'
                return render(request,'login.html',{'msg':msg,'email':email})

        else:
            msg="Email Not registerd"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request,'login.html',{'msg':msg})



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
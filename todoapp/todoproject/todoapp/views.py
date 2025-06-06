
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import User
# Create your views here.

def home(request):
    return render(request,'home.html')




def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        profile = request.FILES.get('profile')  # use FILES for image
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        try:
            if User.objects.filter(user_email=email).exists():
                msg = "Email already exists"
                return render(request, 'register.html', {'key': msg})

            if password != cpassword:
                msg = "Passwords do not match"
                return render(request, 'register.html', {'key': msg})

            # Create user
            user = User.objects.create(
                user_name=username,
                user_email=email,
                user_phone=phone,
                user_dob=dob,
                user_gender=gender,
                user_profile=profile,
                user_pass=password
            )
            msg = "Registration successful"
            print("User created:", user)  
            return render(request, 'login.html', {'key': msg})
        
        except Exception as e:
            print("Registration error:", e)  
            msg = "An error occurred: " + str(e)
            return render(request, 'register.html', {'key': msg})

    return render(request, 'register.html')





def login_view(request):
   pass



def logout_view(request):
    logout(request)
    return redirect('resgister')
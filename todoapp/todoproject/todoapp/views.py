from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        # Basic example, no validation here, add as needed
        if User.objects.filter(user_email=email).exists():
            msg = "Email already registered"
            return render(request, 'register.html', {'msg': msg})

        user = User.objects.create(
            user_name=username,
            user_email=email,
            user_pass=password,
            user_phone=phone,
            user_dob=dob,
            user_gender=gender
        )
        user.save()
        return redirect('login_user')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(user_email=email)
            if user.user_pass == password:
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                msg = "Incorrect password"
        except User.DoesNotExist:
            msg = "Email not registered"

        return render(request, 'login.html', {'msg': msg})

    return render(request, 'login.html')


def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_user')

    user = User.objects.get(id=user_id)
    return render(request, 'dashboard.html', {'user_detail': user})


def logout_user(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('home')

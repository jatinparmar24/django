from django.shortcuts import render, redirect, get_object_or_404
from .models import User,Task


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

    # Fetch user data (optional)
    user = User.objects.get(id=user_id)

    # Fetch tasks belonging to logged-in user
    tasks = Task.objects.filter(user_id=user_id)

    return render(request, 'dashboard.html', {
        'user': user,
        'tasks': tasks,
    })



def logout_user(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('home')

def add_task(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_user')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(user=user, title=title, completed=False)
            return redirect('dashboard')
        else:
            error = "Task title cannot be empty."
            return render(request, 'add_task.html', {'error': error, 'title': title})

    return render(request, 'add_task.html')



def edit_task(request, task_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_user')

    user = User.objects.get(id=user_id)
    task = get_object_or_404(Task, id=task_id, user=user) 

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            task.title = title
            task.save()
            return redirect('dashboard')
        else:
            error = "Task title cannot be empty."
            return render(request, 'edit_task.html', {'task': task, 'error': error})

    return render(request, 'edit_task.html', {'task': task})


    

def delete_task(request, task_id):
    delete_data=Task.objects.get(id=task_id)
    delete_data.delete()
    return redirect('dashboard')


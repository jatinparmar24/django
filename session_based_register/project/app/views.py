from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method=='POST':
        request.session['name']=request.POST.get('name')
        request.session['email']=request.POST.get('email')
        request.session['contact']=request.POST.get('contact')

        return render(request,'login.html')

    else:
        return render(request,'register.html')
    

    


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')

        name1=request.session['name']
        email1=request.session['email']

        if name==name1 and email==email1:
            return render(request,'dashboard.html')
        
        else:
            return render(request,'login.html')

    return render(request,'registration.html')

def dashboard(request):
    return render(request,'dashboard.html')

def sett(request):
    if request.method=='POST':
        request.session['name']=request.POST.get('name')
        request.session['email']=request.POST.get('email')
        request.session['contact']=request.POST.get('contact')

        return render(request,'login.html')







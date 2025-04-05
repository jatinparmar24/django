from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return render('request','home.html')

def home(request):
    # return redirect('/index/')  to jump on http response
    name,city='jatin','sehore'
    # return redirect(f'/index/?name={name}&city={city}')

    # for format
    return redirect('/index/?name={}&city={}'.format(name,city))

def index(request):
    print(request.method)
    print(request.GET)
    # with f string
    # x=request.GET.get('name')
    # y=request.GET.get('city')
    # print(x,y)

    # with format

    x=request.GET.get('name')
    y=request.GET.get('city')
    print(x,y)

    # return HttpResponse("Hello world")

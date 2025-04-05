from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    # data = {'name':'jatin','age':25,"city":'sehore'} 
    #  return render(request, 'home.html',data)
    # single data

    # multiple data
    data=[{'name':'jatin','age':25,"city":'sehore'},{'name':'raj','age':26,"city":'bhopal'}]

    user={'name':'raj','city':'rewa'}

    return render(request, 'home.html',{'key1':user,'key2':data})

def index(request):
    return redirect('https://www.google.com')

def tc(request):
    return HttpResponse("hello World") 

def js(request):
    data={'name':True,'age':False,'city':None}
    return JsonResponse(data)
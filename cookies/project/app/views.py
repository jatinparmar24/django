from django.shortcuts import render

# Create your views here.

def sett(request):
    data=render(request,'sett.html')
    data.set_cookie('name','Jatin')
    data.set_cookie('age','25' ,max_age=20*60*60)
    data.set_cookie('city','Sehore',httponly=True,secure=True)
    return data


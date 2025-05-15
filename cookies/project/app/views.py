from django.shortcuts import render

# Create your views here.

def sett(request):
    data=render(request,'sett.html')
    data.set_cookie('name','Jatin')
    # data.set_cookie('name',request.POST.get('name'))
    data.set_cookie('age','25' ,max_age=20*60*60)
    data.set_cookie('city','Sehore',httponly=True,secure=True)
    return data

def get(request):
    print('get_cookies')
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    city=request.COOKIES['city']

    data={
        'name':name,
        'age':age,
        'city':city,
    }

    return render(request,'sett.html',{'data':data})


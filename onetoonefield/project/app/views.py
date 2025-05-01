from django.shortcuts import render
from .models import *

# Create your views here.


def adhaar(request):
    data=Adhaar.objects.all()   
    # '''.all for all data'''
    print(data.values())  
    #   ''' to get values in dictionary formate'''

    info=Adhaar.objects.get(adharno=632589658745)
    print(info.adharno)
    print(info.createdby)
    print(info.alloted_date)

    x=info.xyz     # it is called reverse accessing where we get info parent in child and we get info of child into parent called forward accessing
    print(x.name)
    print(x.email)
    print(x.contact)
    print(x.adharno)




def citizen(request):
    data1=Citizen.objects.all()
    print(data1)
    print(data1.values())
    print(data1.values_list())   
    # ''' only get values not with key   and also can't send it into table formate''''

    datas=Citizen.objects.get(name='tej')
    print(datas.name)
    print(datas.email)
    print(datas.contact)
    print(datas.adharno)

    # forward access

    x=datas.adharno
    print(x.adharno)
    print(x.createdby)
    print(x.alloted_date)

    


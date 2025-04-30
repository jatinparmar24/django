from django.shortcuts import render
from .models import *

# Create your views here.


def adhaar(request):
    data=Adhaar.objects.all()   '''.all for all data'''
    print(data.values())    ''' to get values in dictionary formate'''

def citizen(request):
    data1=Citizen.objects.all()
    print(data1.values_list())   ''' only get values not with key   and also can't send it into table formate''''

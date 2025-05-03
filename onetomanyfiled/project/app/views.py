from django.shortcuts import render
from .models import *

# Create your views here.

def student(request):
    all_data=Student.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())

    data=Student.objects.get(stuname='jatin')
    print(data.stuname)
    print(data.stuemail)
    print(data.stucontact)
    print(data.studep.depname)
    print(data.studep.depdis)
    print(data.studep.dephod)

def department(request):
    all_data=Department.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())

    data=Department.objects.get(depname='it')
    all_data=data.students.all()
    print(all_data)




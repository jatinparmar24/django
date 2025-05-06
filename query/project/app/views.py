from django.shortcuts import render
from .models import Student

# Create your views here.

def student(request):
    # all() = return multiple values
    all_data=Student.objects.all()[0]  # it support indecing 
    print(all_data)

    all_data=Student.objects.all()[:2] # it support slicing but not negative
    print(all_data)

    all_data=Student.objects.all().reverse()
    print(all_data)
    
    order_by = return multiple values
    all_data=Student.objects.order_by('stu_name') #  in ascending order
    print(all_data)

    all_data=Student.objects.order_by('-stu_name') #  in descending order
    print(all_data)

    #filter() = it return every record which was asked

    all_data=Student.objects.filter(stu_name='vijay',stu_email='vijay@gmail.com')
    print(all_data)

    #exclude() = remove whom we want to remove and get remaining of all data

    all_data=Student.objects.exclude(stu_name='vijay')
    print(all_data)



    print(all_data.values())
    print(all_data.values_list())

    #above method return multiple record  = all , filter, order_by , exclude

    #this method record single record

    all_data=Student.objects.get(stu_name='vijay') # only single in present and if two person with same name then error
    print(all_data)

    all_data=Student.objects.first()  # it return first object
    print(all_data)

    all_data=Student.objects.last()  # it return last object
    print(all_data)

    all_data=Student.objects.create(stu_name='Abhi',stu_email='Abhi@gmail.com',stu_contact=6597456325,stu_city='Rafiqgang')
    print(all_data)   # it create data

    data=Student.objects.first()
    data.delete()

    data=Student.objects.last()
    # it works as a update method in crud
    data.stu_name='jatin'
    data.stu_email='jatin24@gmail.com'
    data.stu_contact=6589658745
    data.stu_city='city'
    data.save()
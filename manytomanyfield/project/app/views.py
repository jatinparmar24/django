from django.shortcuts import render
from .models import *


# Create your views here.


def fuel(request):
    all_data=FuelModel.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())

    data=FuelModel.objects.get(fuel='Petrol')
    print(data.fuel)
    print(data.fuel_name)

def car(request):
    #forward access
    car=CarModel.objects.get(car_name='SUV')
    fuel_type=car.fuel_name.all()

    for fuel in fuel_type:
        print(fuel.fuel_name)


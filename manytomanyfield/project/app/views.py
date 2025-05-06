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

# for both car and fuel and with forward and reverse acces

# def home(request):
#     # forward access (carmodel to fuelmodel)
#     car=CarModel.objects.get(car_name='Toyato')
#     fuel_type=car.fuel_name.all()

#     for fuel in fuel_type:
#         print(fuel.fuel_name)

#     # reverse access from fuel to car model with related name
#     fuel=FuelModel.objects.get(fuel_name='Petrol')
#     car_using_petrol=fuel.cars.all()

#     for car in car_using_petrol:
#         print(car.car_name)
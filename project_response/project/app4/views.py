from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def app4(request):
    # data={'name':'jatin','age':'25'}
    data={'name':True,'age':False,'city':None}
    # diffrence to identify that data is normal data or json data = if we give True and it return true like that it means it is json data
    return JsonResponse(data)
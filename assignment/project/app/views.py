from django.shortcuts import render
import json

# Create your views here.

def tel(request):
    py_data={'name':"Jatin",'age':True,'''active''':False,"anyother":None}
    json_date=json.dumps(py_data)
    print(json_date)

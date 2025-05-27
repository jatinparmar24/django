from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
import io






# serialize and sdeerialize



# @csrf_exempt
def student_list(request): 
    if request.method=='GET':
        stu = Student.objects.all()
        print(type(stu))
        # print("stu=",stu)
        # print("stu.values()=",stu.values())
        # print("stu.values_list()=",stu.values_list())
        # print("stu.values_list(col1,col2,col3)=",stu.values_list('name','city','rollno'))
        serializer = StudentSerializer(stu, many=True)
        # print("Serializer=",serializer)
        # print(serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        # print("Json_data=",json_data)
        return HttpResponse(json_data, content_type='application/json')
        # when we send json data from views then content type must be "application/json"
        # return JsonResponse(serializer.data,safe=False)
        # first argument of JsonResponse should be a dict,otherwise set safe=False
    elif request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')





def student_detail(request, pk):
    user = Student.objects.get(pk=pk)
    # print(type(user))
    # print("Stu_Name=",user.name)
    # print("Stu_City=",user.city)
    # print("Stu_Rollno=",user.rollno)
    serializer = StudentSerializer(user)
    # print("Serializer=",serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # when we send json data from views then content type must be "application/json"
    return JsonResponse(serializer.data,safe=False)
    # first argument of JsonResponse should be a dict,otherwise set safe=False


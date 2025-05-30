from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io






# serialize and deserialize



@csrf_exempt    # we use this for security purpose for method like {post,put/patch,delete}
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
        print(stream)
        python_data=JSONParser().parse(stream)
        print(python_data)
        serializer=StudentSerializer(data=python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')

    elif request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        new_python_data=JSONParser().parse(stream)
        old_id=new_python_data.get('id')
        old_data=Student.objects.get(id=old_id)
        serializer=StudentSerializer(old_data,data=new_python_data)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='PATCH':
        json_data=request.body
        stream=io.BytesIO(json_data)
        new_python_data=JSONParser().parse(stream)
        id=new_python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=new_python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Partially Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        if id:
            stu=Student.objects.get(id=id)
            stu.delete()
            res={'msg':'Data Deleted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        res={'msg':'Id not present in Database'}
        return JsonResponse(res)





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




from .models import Student,Teacher,Worker,Owner
from rest_framework import serializers

    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"  #["id","name","description","active"]    



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"  

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"  

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"  
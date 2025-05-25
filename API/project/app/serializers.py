from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=50)
    rollno=serializers.IntegerField()
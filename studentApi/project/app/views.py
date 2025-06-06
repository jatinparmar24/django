from django.shortcuts import render
from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# authentication and permission

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = StudentSerializer

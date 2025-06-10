from django.shortcuts import render
from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# authentication and permission

class TeacherViewSet(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# to create custom token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
from .serializers import StudentSerializer,TeacherSerializer,WorkerSerializer,OwnerSerializer
from .models import Student,Teacher,Worker,Owner
from rest_framework import viewsets
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
    serializer_class = TeacherSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
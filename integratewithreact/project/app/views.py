# api/views.py
from rest_framework import viewsets
from .models import Registrations
from .serializers import RegistrationSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registrations.objects.all()
    serializer_class = RegistrationSerializer

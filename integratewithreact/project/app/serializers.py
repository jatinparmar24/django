from rest_framework import serializers
from .models import Registrations

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = '__all__'

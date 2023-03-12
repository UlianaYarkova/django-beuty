from rest_framework import serializers
from TypeOfService.models import TypeOfService

class TypeOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= TypeOfService
        fields = '__all__'
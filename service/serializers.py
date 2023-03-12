from rest_framework import serializers
from service.models import Service, FavoriteService
from master.models import Master
from authentication.serializers import UserSerializer

class MasterSerializerForService(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['first_name', 'last_name']

class ServiceSerializer(serializers.ModelSerializer):
    master_data = MasterSerializerForService(source='master', many=True)
    class Meta:
        model= Service
        exclude = ['master']

class FavoriteServiceSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    service_data = ServiceSerializer(source='service')
    class Meta:
        model = FavoriteService
        exclude = ['user', 'service']
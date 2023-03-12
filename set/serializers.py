from rest_framework import serializers
from set.models import Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Set
        fields = '__all__'
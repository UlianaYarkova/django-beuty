from rest_framework.viewsets import ModelViewSet
from TypeOfService.serializers import TypeOfServiceSerializer
from TypeOfService.models import TypeOfService

class TypeOfServiceViewSet(ModelViewSet):
    queryset = TypeOfService.objects.all()
    serializer_class = TypeOfServiceSerializer

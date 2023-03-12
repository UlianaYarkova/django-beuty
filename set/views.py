from rest_framework.viewsets import ModelViewSet
from set.serializers import SetSerializer
from set.models import Set

class SetViewSet(ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

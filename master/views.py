from rest_framework.viewsets import ModelViewSet
from master.serializers import MasterSerializer
from master.models import Master

class MasterViewSet(ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

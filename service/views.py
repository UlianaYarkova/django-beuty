from rest_framework.viewsets import ModelViewSet
from service.serializers import ServiceSerializer, FavoriteServiceSerializer
from service.models import Service, FavoriteService
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favorite')
    def toggle_favorite(self, requst, pk=None):
        user = requst.user 
        try:
            service = self.queryset.get(pk=pk)
        except Service.DoesNotExist:
            raise NotFound('Service not found')
        try:
            fav_service = FavoriteService.objects.filter(user=user, service=service)
            fav_service.delete()
            return Response ({'messege': 'removed'})
        except FavoriteService.DoesNotExist:
            FavoriteService.objects.create(user=user, service=service)
            return Response({'message': 'added'})
        
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favorites')
    def get_favorite(self, requst):
        user = requst.user 
        service = FavoriteService.objects.filter(user=user)
        data = FavoriteServiceSerializer(data=service, many=True).data
        return Response(data)
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response ({'message': 'success'})
    
    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email must not be empty'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'password must not be empty'})
        
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})
        
        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})
        
        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response
        
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)
    
    @action(methods=['POST'], detail=False, url_path='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        response = Response()
        response.delete_cookie('refresh')
        return response
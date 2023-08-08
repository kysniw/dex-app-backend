from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (UserSerializer, AuthTokenSerializer)
from .models import User


class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        request = self.request.GET(User.objects.all())
        return self.list(request, *args, **kwargs)


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

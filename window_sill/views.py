from rest_framework import authentication, permissions, viewsets

from window_sill import serializers
from window_sill.models import WindowSill


class WindowSillView(viewsets.ModelViewSet):
    serializer_class = serializers.WindowSillSerializer
    queryset = WindowSill.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.WindowSillListSerializer

        return self.serializer_class


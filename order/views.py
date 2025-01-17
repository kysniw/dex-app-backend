from rest_framework import authentication, permissions, viewsets

from .models import Order
from .serializers import OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = Order.objects.filter(user = self.request.user)
        return queryset

    def get_permissions(self):
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
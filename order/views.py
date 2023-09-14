from rest_framework import authentication, permissions, viewsets

from .models import Order, OrderDetail
from .serializers import OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Order.objects.all()

    def get_object(self):
        return self.request.user


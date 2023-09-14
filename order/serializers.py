from rest_framework import serializers
from order import models

from window_sill.serializers import WindowSillListSerializer


class OrderDetailSerializer(serializers.ModelSerializer):

    window_sill = WindowSillListSerializer(many=False, required=True)

    class Meta:
        model = models.OrderDetail
        fields = ['sill_width', 'sill_thickness', 'sill_length', 'price',
                  'description', 'technical_draw', 'window_sill']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):

    order_details = OrderDetailSerializer(many=True, required=True)

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ['id', 'user']

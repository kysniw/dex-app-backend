from rest_framework import serializers
from order import models

from window_sill.serializers import WindowSillListSerializer


class OrderDetailSerializer(serializers.ModelSerializer):

    # window_sill = WindowSillListSerializer(many=False, required=True)

    class Meta:
        model = models.OrderDetail
        fields = ['sill_width', 'sill_thickness', 'sill_length', 'price',
                  'description', 'technical_draw', 'window_sill']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):

    order_details = OrderDetailSerializer(many=True, required=True)

    class Meta:
        model = models.Order
        fields = ['order_details', 'order_status', 'total_price', 'postal_code',
                  'city', 'street', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        order_details_data = validated_data.pop('order_details')
        auth_user = self.context['request'].user
        order = models.Order.objects.create(user=auth_user, **validated_data)
        for order_detail in order_details_data:
            models.OrderDetail.objects.create(order=order, **order_detail)

        return order

from rest_framework import serializers
from product.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'phone_number', 'shipping_address','quantity', 'product', 'total_price']







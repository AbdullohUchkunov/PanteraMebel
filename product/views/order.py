from product.models import Order
from rest_framework import generics
from product.serializers import OrderSerializer


class OrderListApiView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer





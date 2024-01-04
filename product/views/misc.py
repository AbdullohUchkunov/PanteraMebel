from rest_framework import serializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from product.models import ReviewUsers, FlashSale


class CustomPagination(PageNumberPagination):
    page_size = 8


class ReviewUserListCreateView(generics.ListCreateAPIView):
    queryset = ReviewUsers.objects.all()

    class ReviewUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = ReviewUsers
            fields = '__all__'

    serializer_class = ReviewUserSerializer


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale

    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ['id', 'product', 'discount_percentage', 'start_time', 'end_time']

    serializer_class = FlashSaleSerializer





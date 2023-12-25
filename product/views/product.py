from django.db import models
from django_filters import rest_framework as django_filters
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from product.filters import ProductFilter
from product.models import Product, Category
from product.permissions import IsStaffOrReadOnly
from product.serializers import ProductSerializer, CategorySerializer


class CustomPagination(PageNumberPagination):
    page_size = 4


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    pagination_class = CustomPagination

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', 'None')
        if category:
            self.queryset = self.queryset.filter(category=category)
        return super().list(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



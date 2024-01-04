from django_filters import rest_framework as django_filters
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from product.filters import ProductFilter
from product.models import Product, Category,SubCategory
from product.serializers import ProductSerializer, CategorySerializer,SubCategorySerializer
from rest_framework.generics import ListAPIView


class CustomPagination(PageNumberPagination):
    page_size = 4


class ProductViewSet(viewsets.ModelViewSet):
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_products = Product.objects.filter(category=instance.category).exclude(id=instance.id)[:5]
        related_serializer = ProductSerializer(related_products, many=True)
        return Response({
            'product': serializer.data,
            'related_products': related_serializer.data
        })


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductListByCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


class SubCategoryByCategory(ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        sub_category_id = self.kwargs['sub_category_id']
        return SubCategory.objects.filter(sub_category=sub_category_id)

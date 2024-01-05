from rest_framework import serializers
from product.models import Category,Product,SubCategory,ProductPhotoView,ProductPhotoColor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']


class ProductPhotoColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotoColor
        fields = '__all__'


class ProductPhotoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotoView
        fields = '__all__'


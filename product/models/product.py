from django.db import models
from modeltranslation.translator import TranslationOptions
from modeltranslation.fields import TranslationField


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    sub_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(SubCategory, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductPhotoColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imagesColor', null=True)

    def __str__(self):
        return f"{self.product} - {self.color}"


class ProductPhotoView(models.Model):
    photo = models.ForeignKey(ProductPhotoColor, on_delete=models.CASCADE)
    photoBack = models.ImageField(upload_to='imageView')
    photoFront = models.ImageField(upload_to='imageView')
    photoRight = models.ImageField(upload_to='imageView')
    photoLeft = models.ImageField(upload_to='imageView')










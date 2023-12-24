from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)












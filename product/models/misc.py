from django.db import models
from django.utils import timezone
from .product import Product


class ReviewUsers(models.Model):
    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()


class FlashSale(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    class Meta:
        unique_together = ('product', 'start_time', 'end_time')





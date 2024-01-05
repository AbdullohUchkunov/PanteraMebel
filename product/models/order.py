from django.db import models
from .product import Product
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxxxx'."
)


class Order(models.Model):
    customer = models.CharField(max_length=25)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, null=True)
    shipping_address = models.TextField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} - {self.customer} - {self.phone_number}"












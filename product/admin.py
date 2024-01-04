from django.contrib import admin
from .models import Product, Category, SubCategory, ReviewUsers, FlashSale

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(FlashSale)
admin.site.register(ReviewUsers)




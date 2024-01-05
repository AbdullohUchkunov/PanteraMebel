from django.contrib import admin
from .models import Product, Category, SubCategory, ReviewUsers, FlashSale
from modeltranslation.admin import TranslationAdmin


admin.register(FlashSale)
admin.register(ReviewUsers)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ('name',)




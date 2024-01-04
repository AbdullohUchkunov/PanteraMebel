from modeltranslation.translator import translator, TranslationOptions
from .models import Category,SubCategory,Product


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description')


translator.register(Category, CategoryTranslationOptions)
translator.register(SubCategory,SubCategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
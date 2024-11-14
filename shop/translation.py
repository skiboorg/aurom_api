from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'short_description',
    )

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'country',
        'delivery',
        'name',
        'short_description',
        'in_stock',
        'unit',
        'price_description',
        'description',
    )
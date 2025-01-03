from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Sale)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'content',
    )


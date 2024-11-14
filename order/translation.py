from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Delivery)
class DeliveryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )

@register(Payment)
class PaymentTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
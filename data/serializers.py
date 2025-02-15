from rest_framework import serializers
from .models import *
from shop.serializers import ProductShortSerializer

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer(many=True, read_only=True)
    class Meta:
        model = Sale
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'



class CallbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackForm
        fields = '__all__'

        extra_kwargs = {
            "name": {"error_messages": {"required": "Имя обязательное поле"}, 'required': True},
            'email': {"error_messages": {"required": "Email обязательное поле"},'required': True},
            'phone': {"error_messages": {"required": "Телефон обязательное поле"},'required': True},
            'file': {'required': False},
        }
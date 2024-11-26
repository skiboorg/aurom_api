from rest_framework import exceptions, serializers, status, generics


from .models import *


class NewsItemShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        exclude = ['content_editor','content']


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'












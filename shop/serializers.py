from rest_framework import exceptions, serializers, status, generics


from .models import *
from django.conf import settings



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['name_en', 'name_ru']

class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(many=True,required=False,read_only=True)
    files = ProductFileSerializer(many=True,required=False,read_only=True)
    cat_slug = serializers.SerializerMethodField()
    cat_name = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, required=False, read_only=True)
    exclude = ['description_editor']

    class Meta:
        model = Product
        fields = '__all__'
    def get_cat_slug(self,obj):
        return obj.category.slug
    def get_cat_name(self,obj):
        return obj.category.name


class ProductShortSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'article',
            'is_new',
            'is_in_stock',
            'image',
            'name',
            'slug',
            'in_stock',
            'unit',
            'price_description',
            'country',
            'price'

        ]
    def get_image(self,obj):
        main_image = obj.images.filter(is_main=True)
        if main_image.exists():
            return f'{settings.IMG_URL}{main_image.first().image.url}'
        else:
            return None






class CategorySerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image','top_image','name','slug','short_description','display_amount']

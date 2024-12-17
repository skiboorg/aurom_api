from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework import generics
from .models import *

# class GetInstructions(APIView):
#     def get(self, request):
#         return Response("Hello World")


class GetCategories(generics.ListAPIView):
    serializer_class = CategoryShortSerializer
    queryset = Category.objects.all()



class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = 'slug'


class GetProduct(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    lookup_field = 'slug'



class GetPopularProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.filter(is_popular=True, is_active=True)

class ProductSearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')  # Получаем значение параметра "q" из GET-запроса
        # Базовый запрос для поиска активных продуктов
        products = Product.objects.filter(is_active=True)
        products = products.filter(
            Q(name__icontains=query) |
            Q(article__icontains=query)
        ).distinct()
        serializer = ProductShortSerializer(products, many=True)
        return Response(serializer.data)
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
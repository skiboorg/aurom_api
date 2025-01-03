import json
from decimal import Decimal

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser

class GetBanners(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class NewForm(generics.CreateAPIView):
    queryset = CallbackForm
    serializer_class = CallbackFormSerializer
    # parser_classes = MultiPartParser




class GetSales(generics.RetrieveAPIView):
    serializer_class = SaleSerializer

    def get_object(self):
        sale_type = self.request.query_params.get('sale_type')
        if sale_type == 'sale':
            return Sale.objects.get(is_sale=True,is_active=True)
        else:
            return Sale.objects.get(is_sale=False,is_active=True)


class GetCourses(generics.RetrieveAPIView):
    serializer_class = CurrencySerializer

    def get_object(self):
        return Currency.objects.all().first()

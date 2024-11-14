from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from cart.views import get_cart
from .serializers import *
from .models import *


class OrderView(APIView):
    def get(self, request):
        print(request.data)
        result = {}
        return Response(status=200)

    def delete(self, request):
        print(request.data)
        result = {}
        return Response(status=200)

    def patch(self, request):
        print(request.data)
        result = {}
        return Response(result,status=200)

    def post(self, request):
        data = request.data
        print(data)
        cart = get_cart(request)
        payment_type_id = data.get('payment',None)
        delivery_type_id = data.get('delivery',None)
        if not payment_type_id:
            payment_type_id = Payment.objects.first().id
            delivery_type_id = Delivery.objects.first().id
        new_order = Order.objects.create(
            customer=data['fio'],
            phone=data['phone'],
            email=data['email'],
            comment=data['comment'],
            payment_type_id=payment_type_id,
            delivery_type_id=delivery_type_id,
            delivery_address=data['delivery_address']
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=new_order,
                article=item.product.article,
                name=item.product.name,
                unit=item.product.unit,
                price=item.product.price,
                amount=item.amount
            )
            item.delete()
        result = {'result': True, 'message': f'Заказ {new_order.id} создан'}
        return Response(result, status=200)


class GetDeliveries(generics.ListAPIView):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()

class GetPayments(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
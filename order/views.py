import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from cart.views import get_cart
from .serializers import *
from .models import *
from yookassa import Configuration, Payment as YooPayment
import settings
import uuid
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
        payment_type = Payment.objects.get(id=payment_type_id)
        if not payment_type_id:
            payment_type = Payment.objects.first()
            delivery_type_id = Delivery.objects.first().id
        new_order = Order.objects.create(
            customer=data['fio'],
            phone=data['phone'],
            email=data['email'],
            comment=data['comment'],
            payment_type=payment_type,
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

        if not payment_type.is_online:
            result = {'result': True, 'message': f'Заказ {new_order.id} создан'}
            return Response(result, status=200)

        Configuration.account_id = settings.shopID
        Configuration.secret_key = settings.secretKey
        Configuration.configure(settings.shopID, settings.secretKey)

        items = []

        for item in new_order.items.all():
            items.append({
                "description": item.name,
                "quantity": item.amount,
                "amount": {
                    "value": Decimal(item.price),
                    "currency": "RUB"
                },
                "vat_code": 2,
                "payment_mode": "full_prepayment",
                "payment_subject": "commodity"
            })

        payment = YooPayment.create({
            "amount": {
                "value": new_order.total_price,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": f"https://laurom.ru"
            },
            "receipt": {
                "customer": {
                    "full_name": new_order.customer,
                    "phone": new_order.phone
                },
                "items": items
            },
            "capture": True,
            "description": f"Оплата заказа {new_order.id}"
        }, uuid.uuid4())

        response = json.loads(payment.json())
        print(response)
        formUrl = response['confirmation']['confirmation_url']
        payment_id = response.get('id')
        if formUrl:
            PaymentObj.objects.create(payment_id=payment_id,
                                   order=new_order,
                                   amount=new_order.total_price)
            return Response({
                'result': True,
                'formUrl': formUrl,
                'p_id': payment_id
            },
                status=200)
        else:
            result = {'result': False, 'message': f'Ошибка'}
            return Response(result, status=200)

class GetDeliveries(generics.ListAPIView):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()

class GetPayments(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
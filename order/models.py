from django.db import models
from decimal import Decimal
from django_resized import ResizedImageField


class Delivery(models.Model):
    name = models.CharField('Название доставки',max_length=255)
    image = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/order/delivery',
                              blank=False, null=True)
    description = models.TextField('Описание доставки', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'


class Payment(models.Model):
    name = models.CharField('Название оплаты', max_length=255)
    image = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/order/payment',
                              blank=False, null=True)
    description = models.TextField('Описание оплаты', blank=True, null=True)
    is_online = models.BooleanField(default=False, null=False)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'


class Order(models.Model):
    order_id = models.CharField('Номер заказа', max_length=255, blank=True, null=True)
    customer = models.CharField('ФИО', max_length=255, blank=True, null=True)
    phone = models.CharField('контактный телефон', max_length=255, blank=True, null=True)
    email = models.CharField('почта', max_length=255, blank=True, null=True)
    comment = models.TextField('комментарий к заказу', blank=True, null=True)
    payment_type = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    delivery_type = models.ForeignKey(Delivery, on_delete=models.SET_NULL, blank=True, null=True)
    delivery_address = models.TextField('адрес доставки', blank=True, null=True)
    created_at = models.DateTimeField('Создан',auto_now_add=True, null=True)
    is_paid = models.BooleanField('Оплачен', default=False, null=False)
    is_done = models.BooleanField('Обработан', default=False, null=False)
    is_deliveried = models.BooleanField('Доставлен', default=False, null=False)

    @property
    def total_price(self):
        price = 0
        for item in self.items.all():
            price += Decimal(item.price) * item.amount
        return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    article = models.CharField('Артикул', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    unit = models.CharField('Ед. измерения', max_length=255, blank=False, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)



class PaymentObj(models.Model):
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    order = models.ForeignKey(Order,
                              blank=True,
                              null=True,
                              default=None,
                              on_delete=models.CASCADE,
                              verbose_name='Заказ',
                              related_name='order_payment')
    status = models.BooleanField(default=False)
    amount = models.DecimalField(default=0,decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
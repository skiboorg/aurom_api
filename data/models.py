from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field
from shop.models import Product




class Currency(models.Model):
    eurRub = models.DecimalField(max_digits=6, decimal_places=2)
    eurUsd = models.DecimalField(max_digits=6, decimal_places=2)


class Sale(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)

    content_editor = CKEditor5Field('Редактор', blank=True, null=True, config_name='extends')
    content = models.TextField('Контент', blank=True, null=True)
    is_sale = models.BooleanField('Это распродажа', default=False, null=False)
    is_active = models.BooleanField('Активно', default=False, null=False)
    product = models.ManyToManyField(Product, blank=False)

    def __str__(self):
        return f'{self.name}'



    class Meta:
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'


class CallbackForm(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=False, null=True)
    name = models.CharField('Имя',max_length=255,blank=False, null=True)
    email= models.EmailField('email',max_length=255,blank=False, null=True)
    phone= models.CharField('Телефон',max_length=255,blank=False, null=True)
    subject= models.CharField('Тема',max_length=255,blank=True, null=True)
    text = models.TextField('Текст',blank=True, null=True)
    file= models.FileField('Файл',upload_to='forms',blank=True, null=True)
    is_done = models.BooleanField('Обработана', default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Banner(models.Model):
    order_num = models.IntegerField(default=10)
    image_big = ResizedImageField('Баннер десктоп', size=[1440, 640], quality=95, force_format='WEBP', upload_to='banner/images',
                              blank=False, null=True)
    image_small = ResizedImageField('Баннер мобилка', size=[760, 640], quality=95, force_format='WEBP',
                                 upload_to='banner/images',
                                 blank=False, null=True)
    text_big = models.TextField('Текст большой', blank=True, null=True)
    text_small = models.TextField('Текст маленький', blank=True, null=True)
    def __str__(self):
        return f'{self.order_num}'



    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['order_num']


from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField




class Category(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = models.FileField(upload_to='shop/category/images', blank=True, null=True)
    # image = ResizedImageField(size=[60, 100], quality=95, force_format='WEBP', upload_to='shop/category/images',
    #                           blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=True, null=False)
    slug = models.CharField('ЧПУ', max_length=255,blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)
    display_amount = models.IntegerField(default=0, blank=True, null=True)

    html_content_ru = models.TextField('SEO текст [RU]', blank=True, null=True)
    html_content_en = models.TextField('SEO текст [EN]', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    article = models.CharField('Артикул', max_length=20,blank=True, null=True)
    country = models.CharField('Страна производства', max_length=100, blank=True, null=True)
    delivery = models.CharField('Срок поставки', max_length=100, blank=True, null=True)
    in_stock = models.CharField('В наличии' ,max_length=100, blank=True, null=True)
    unit = models.CharField('Фасовка', max_length=255, blank=True, null=True)
    price = models.DecimalField('Цена EURO', default=0, decimal_places=2,max_digits=10, blank=True)
    price_usd = models.DecimalField('Цена $', default=0,decimal_places=2,max_digits=10, blank=True)
    price_rub = models.DecimalField('Цена RUB', default=0, decimal_places=2,max_digits=10, blank=True)
    price_opt = models.DecimalField('Цена опт', default=0, decimal_places=2,max_digits=10, blank=True)
    price_description = models.CharField('Описание цены', blank=True, null=True, max_length=200)

    is_new = models.BooleanField('Новинка', default=False, null=False)
    is_in_stock = models.BooleanField('В наличии?', default=True, null=False)
    is_popular = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    description_editor = CKEditor5Field('Редактор', blank=True, null=True, config_name='extends')
    description = models.TextField('Описание', blank=True, null=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='images')
    image = ResizedImageField(size=[650, 570], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    is_main = models.BooleanField('Основное', default=False, null=False)

    def __str__(self):
        return f''

    class Meta:

        verbose_name = 'Доп. изображение товара'
        verbose_name_plural = 'Доп. изображения товара'

class ProductUnit(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='units')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    price_description = models.CharField('Описание цены', blank=True, null=True, max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Фасовка'
        verbose_name_plural = 'Фасовка'

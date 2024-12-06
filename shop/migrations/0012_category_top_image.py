# Generated by Django 5.1.3 on 2024-12-05 10:57

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_category_image_alter_product_price_opt'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='top_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[1380, 300], upload_to='shop/category/images'),
        ),
    ]

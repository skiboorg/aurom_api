# Generated by Django 5.1.3 on 2024-11-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_price_alter_product_price_opt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='shop/category/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_opt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена опт'),
        ),
    ]

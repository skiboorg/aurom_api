# Generated by Django 5.1.3 on 2024-11-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_price_rub_product_price_usd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена EURO'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_opt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Цена опт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_rub',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена RUB'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена $'),
        ),
    ]

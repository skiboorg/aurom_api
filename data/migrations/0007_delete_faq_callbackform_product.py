# Generated by Django 5.1.3 on 2024-11-17 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_callbackform_is_done'),
        ('shop', '0009_product_price_rub_product_price_usd_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Faq',
        ),
        migrations.AddField(
            model_name='callbackform',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]

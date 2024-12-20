# Generated by Django 5.1.3 on 2024-11-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_name_alter_category_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='В наличии'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание цены'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(max_length=255, null=True, verbose_name='Фасовка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]

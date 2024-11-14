# Generated by Django 5.1.3 on 2024-11-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, editable=False, max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
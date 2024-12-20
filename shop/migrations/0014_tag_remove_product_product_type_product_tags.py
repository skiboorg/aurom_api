# Generated by Django 5.1.3 on 2024-12-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_product_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, max_length=100, related_name='Теги', to='shop.tag'),
        ),
    ]

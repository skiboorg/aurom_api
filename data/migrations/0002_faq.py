# Generated by Django 5.0.2 on 2024-03-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=10)),
                ('question', models.CharField(max_length=255, null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faq',
                'ordering': ['order_num'],
            },
        ),
    ]

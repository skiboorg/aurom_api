# Generated by Django 5.1.4 on 2025-02-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]

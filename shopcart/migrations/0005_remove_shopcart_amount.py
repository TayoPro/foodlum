# Generated by Django 4.0.2 on 2022-02-28 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0004_shopcart_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='amount',
        ),
    ]

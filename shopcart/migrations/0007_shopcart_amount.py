# Generated by Django 4.0.2 on 2022-02-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0006_remove_shopcart_spicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]

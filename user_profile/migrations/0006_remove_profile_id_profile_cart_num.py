# Generated by Django 4.0.2 on 2022-03-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='cart_num',
            field=models.AutoField(default=1001, primary_key=True, serialize=False),
        ),
    ]
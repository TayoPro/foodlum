# Generated by Django 4.0.2 on 2022-02-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0008_contact_remove_meal_spicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

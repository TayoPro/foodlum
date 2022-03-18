# Generated by Django 4.0.2 on 2022-02-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0007_alter_meal_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Closed', 'Closed')], default='New', max_length=100)),
                ('closed', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='meal',
            name='spicy',
        ),
    ]

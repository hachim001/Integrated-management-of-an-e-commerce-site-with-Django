# Generated by Django 4.2.1 on 2023-06-13 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_creation',
        ),
    ]
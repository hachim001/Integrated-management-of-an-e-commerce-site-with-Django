# Generated by Django 4.2.1 on 2023-06-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img/avatar1.png', upload_to='profile/'),
        ),
    ]
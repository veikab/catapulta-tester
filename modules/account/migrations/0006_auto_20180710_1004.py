# Generated by Django 2.0.6 on 2018-07-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180710_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='avatars/default-user.png', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]

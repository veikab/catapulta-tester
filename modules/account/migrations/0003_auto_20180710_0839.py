# Generated by Django 2.0.6 on 2018-07-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180710_0823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунт'},
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='default-user.png', upload_to='media/avatars/', verbose_name='Аватар'),
        ),
    ]

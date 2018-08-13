# Generated by Django 2.0.7 on 2018-08-13 08:50

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20180731_0643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунт'},
        ),
        migrations.AlterModelOptions(
            name='customgroup',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='custompermission',
            options={'ordering': ('content_type__app_label', 'content_type__model', 'codename'), 'verbose_name': 'Разрешение', 'verbose_name_plural': 'Разрешения'},
        ),
        migrations.AddField(
            model_name='customgroup',
            name='verified',
            field=models.BooleanField(default=True, verbose_name='Потвержденный'),
        ),
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=image_cropping.fields.ImageCropField(default='avatars/default-user.png', upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Почтовый адрес'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группа к которой принадлежит пользователь', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', related_query_name='user', to='account.CustomGroup', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='account',
            name='second_name',
            field=models.CharField(max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Выставить права пользователю.', related_name='user_set', related_query_name='user', to='account.CustomPermission', verbose_name='Права пользователя'),
        ),
        migrations.AlterField(
            model_name='customgroup',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='customgroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='account.CustomPermission', verbose_name='разешения'),
        ),
        migrations.AlterField(
            model_name='custompermission',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
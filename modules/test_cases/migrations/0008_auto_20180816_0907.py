# Generated by Django 2.0.7 on 2018-08-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_cases', '0007_auto_20180814_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('0', 'Провалено'), ('1', 'Успешно'), ('2', 'Не выполнялось')], default='0', max_length=20, verbose_name='Статус'),
        ),
    ]
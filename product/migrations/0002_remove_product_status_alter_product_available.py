# Generated by Django 4.2 on 2023-11-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(choices=[(False, 'Нет в наличии'), (True, 'В наличии')], default=1, verbose_name='Статус'),
        ),
    ]

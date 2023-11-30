# Generated by Django 4.2 on 2023-11-23 15:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Url категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название модели')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Url модели')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_models', to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Артикуль')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('color_product', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет товара')),
                ('color_strap', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет ремешка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара, руб.')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Фото')),
                ('weight_product', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вес товара, г')),
                ('size_product', models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер товара')),
                ('built_in_memory', models.CharField(max_length=100, verbose_name='Встроенная память')),
                ('number_of_sim_cards', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество SIM - карт')),
                ('housing_material', models.CharField(blank=True, max_length=100, null=True, verbose_name='Материал корпуса')),
                ('display_diagonal', models.CharField(max_length=100, verbose_name='Диагональ дисплея')),
                ('ram', models.CharField(max_length=100, verbose_name='Оперативная память')),
                ('display_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип дисплея')),
                ('number_of_processor_cores', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество ядер процессора')),
                ('port', models.CharField(blank=True, max_length=100, null=True, verbose_name='Порт')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Производитель')),
                ('complete_set', models.CharField(blank=True, max_length=100, null=True, verbose_name='Комплектация')),
                ('video_adapter', models.CharField(blank=True, max_length=100, null=True, verbose_name='Видеоадаптер')),
                ('stock', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Количество на складе')),
                ('status', models.BooleanField(choices=[(0, 'Нет в наличии'), (1, 'В наличии')], default=1)),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('delivery', models.BooleanField(default=True, verbose_name='Возможоность доставки')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category', verbose_name='Категория')),
                ('product_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='models', to='product.productmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['-date'],
                'index_together': {('id', 'sku')},
            },
        ),
    ]

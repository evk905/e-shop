from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории, к которым относятся товары"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Url категории')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_category', kwargs={'product_category_slug': self.slug})


class Product(models.Model):
    """Модель описания продукта"""

    objects = models.Manager()

    class Status(models.IntegerChoices):
        OUT_OF_STOCK = 0, 'Нет в наличии'
        IN_STOCK = 1, 'В наличии'

    slug = models.CharField(max_length=150, unique=True, verbose_name='Артикуль', db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products',
                                 verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    color_product = models.CharField(max_length=100, verbose_name='Цвет товара', blank=True, null=True)
    color_strap = models.CharField(max_length=100, verbose_name='Цвет ремешка', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара, руб.')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    weight_product = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес товара, г')
    size_product = models.CharField(max_length=100, verbose_name='Размер товара', blank=True, null=True)
    built_in_memory = models.CharField(max_length=100, verbose_name='Встроенная память')
    number_of_sim_cards = models.CharField(max_length=100, verbose_name='Количество SIM - карт', blank=True, null=True)
    housing_material = models.CharField(max_length=100, verbose_name='Материал корпуса', blank=True, null=True)
    display_diagonal = models.CharField(max_length=100, verbose_name='Диагональ дисплея')
    ram = models.CharField(max_length=100, verbose_name='Оперативная память')
    display_type = models.CharField(max_length=100, verbose_name='Тип дисплея', blank=True, null=True)
    number_of_processor_cores = models.CharField(max_length=100, verbose_name='Количество ядер процессора', blank=True,
                                                 null=True)
    port = models.CharField(max_length=100, verbose_name='Порт', blank=True, null=True)
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель', blank=True, null=True)
    complete_set = models.CharField(max_length=100, verbose_name='Комплектация', blank=True, null=True)
    video_adapter = models.CharField(max_length=100, verbose_name='Видеоадаптер', blank=True, null=True)
    stock = models.PositiveIntegerField(default=1, verbose_name='Количество на складе', blank=True, null=True)
    available = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                    verbose_name='Статус', default=Status.IN_STOCK)
    delivery = models.BooleanField(default=True, verbose_name='Возможоность доставки')

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-date']),
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_detail_slug': self.slug})

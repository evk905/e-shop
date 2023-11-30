from django.db import models
from django.urls import reverse
from product.models import Product


class Delivery(models.Model):
    """Модель описания доставки"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='deliveries', verbose_name='Продукт')
    delivery_type = models.CharField(max_length=100, verbose_name='Тип доставки')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена доставки, руб.')
    duration = models.CharField(max_length=100, verbose_name='Срок доставки')
    tracking_number = models.CharField(max_length=100, unique=True, verbose_name='Номер отслеживания')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return f"{self.delivery_type} для {self.product.name}"

    def get_absolute_url(self):
        return reverse('delivery_detail', kwargs={'tracking_number': self.tracking_number})

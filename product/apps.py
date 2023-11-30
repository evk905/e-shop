from django.apps import AppConfig


class ProductConfig(AppConfig):
    verbose_name = "Каталог товаров"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

from django.contrib import admin, messages

from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("category", )
    search_fields = ('name', )
    list_display = ('slug', 'name', 'category', 'price', 'date', 'stock',  'available', 'delivery')
    list_display_links = ('name',)
    ordering = ['-date', 'name']
    list_editable = ('available', 'category', 'delivery')
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}




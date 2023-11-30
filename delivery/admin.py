from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('product', 'delivery_type', 'price', 'duration', 'tracking_number')
    list_display_links = ('tracking_number',)
    search_fields = ('product__name', 'tracking_number')
    list_filter = ('delivery_type',)
    ordering = ['product__name']
    list_per_page = 10
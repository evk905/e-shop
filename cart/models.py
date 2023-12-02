from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
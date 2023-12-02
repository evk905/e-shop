from django.urls import path
from .views import CartAPIView, AddToCartView

urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]






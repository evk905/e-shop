
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm


#
# class CartFormView(View):
#     """Представление для добавления товаров через форму
#     Представление для удаления 1 шт. товара из корзины"""
#     http_method_names = ['post', 'get']
#
#     def post(self, request, product_id):
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)
#         form = CartAddProductForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             cart.add(product=product,
#                      quantity=cd['quantity'],
#                      update_quantity=cd['update'])
#         return redirect('cart:cart_detail')
#
#     def get(self, request, product_id):
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)
#         cart.remove(product)
#         return redirect('cart:cart_detail')

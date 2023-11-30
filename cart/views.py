from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CouponApplyForm

from .recommender import Recommender  # Подключите ваш класс рекомендаций


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity': item['quantity'],
                'override': True
            })
        coupon_apply_form = CouponApplyForm()

        r = Recommender()
        cart_products = [item['product'] for item in cart]
        if cart_products:
            recommended_products = r.suggest_products_for(cart_products, max_results=4)
        else:
            recommended_products = []

        return render(request, 'cart/detail.html', {
            'cart': cart,
            'coupon_apply_form': coupon_apply_form,
            'recommended_products': recommended_products
        })


class CartAddView(View):
    """Представление для добавления товаров через форму"""
    http_method_names = ['post']

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart:cart_detail')


class CartRemoveView(View):
    """Представление для удаления 1 шт. товара из корзины"""

    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')



from .models import CartItem

class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in self.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}

        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = CartItem.objects.filter(id__in=product_ids)
        cart_items = self.cart.values()

        for product, cart_item in zip(products, cart_items):
            yield {
                'product': product,
                'quantity': cart_item['quantity']
            }

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
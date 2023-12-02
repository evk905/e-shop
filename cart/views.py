from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .cart import Cart
from .serializes import CartItemSerializer


class CartAPIView(APIView):
    def get(self, request):
        cart = Cart(request)
        cart_items = cart.__iter__()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = Cart(request)
        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            product_id = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']
            cart.add(product_id, quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)  # Если количество не указано, по умолчанию считаем 1
        cart = Cart(request)
        cart.add(product_id, quantity)
        return Response({'message': 'Товар успешно добавлен в корзину'}, status=status.HTTP_200_OK)
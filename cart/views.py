from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .cart import Cart
from .serializes import CartItemSerializer


class CartAPIView(APIView):
    def get(self, request):
        cart = Cart(request)
        cart_contents = [{'product_id': item['product_id'], 'quantity': item['quantity']} for item in cart]
        serializer = CartItemSerializer(cart_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            cart = Cart(request)
            cart.add(product_id, quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            cart = Cart(request)
            cart.add(product_id, quantity, update_quantity=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            cart = Cart(request)
            cart.remove(product_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

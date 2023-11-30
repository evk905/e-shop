from django.urls import path
from .views import CartAddView, CartRemoveView
# from .views import CartDetailView

app_name = 'cart'

urlpatterns = [
    # path('view/', CartDetailView.as_view(), name='cart'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('remove/<int:product_id>', CartRemoveView.as_view(), name='cart_remove'),

]









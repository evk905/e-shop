from django.urls import path, include
from .views import index
from .views import ProductListView, ProductDetailView, CategoryListlView
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('', index, name='ishop'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('product/<slug:product_detail_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:product_category_slug>/', CategoryListlView.as_view(), name='product_category'),
    path('api/', include(router.urls)),

]




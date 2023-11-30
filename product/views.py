from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Product, Category
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer


def index(request):
    return HttpResponse("Главная страница")


class ProductListView(ListView):
    """View для каталога товаров"""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    """View для детальной страницы товара"""
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_detail_slug'


class CategoryListlView(ListView):
    """View для категории товаров"""
    model = Category
    template_name = 'categoty/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['product_category_slug'])


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

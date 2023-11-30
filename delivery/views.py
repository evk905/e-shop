from rest_framework import generics
from django.views.generic import ListView, DetailView
from .serializes import DeliverySerializer
from .models import Delivery


class DeliveryListView(ListView):
    """View для списка доставок"""
    model = Delivery
    template_name = 'deliveries/delivery_list.html'
    context_object_name = 'deliveries'
    paginate_by = 10

    def get_queryset(self):

        return Delivery.objects.all()


class DeliveryDetailView(DetailView):
    """View для детальной страницы доставки"""
    model = Delivery
    template_name = 'deliveries/delivery_detail.html'
    context_object_name = 'delivery'
    slug_field = 'tracking_number'
    slug_url_kwarg = 'tracking_number'


class DeliveryList(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryDetail(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'tracking_number'

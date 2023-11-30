from django.urls import path
from .views import DeliveryListView, DeliveryDetailView, DeliveryList, DeliveryDetail

urlpatterns = [

    path('deliveries/', DeliveryListView.as_view(), name='delivery_list'),
    path('deliveries/<slug:tracking_number>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('api/deliveries/', DeliveryList.as_view(), name='delivery-list'),
    path('api/deliveries/<str:tracking_number>/', DeliveryDetail.as_view(), name='delivery-detail'),
]
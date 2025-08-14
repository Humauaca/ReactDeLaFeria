from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = models.ShippingInfo.objects.all()
    serializer_class = serializers.ShippingSerializer

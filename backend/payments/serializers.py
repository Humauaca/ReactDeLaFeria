from rest_framework import serializers
from . import models

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class ShippingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ShippingInfo
        fields = '__all__'
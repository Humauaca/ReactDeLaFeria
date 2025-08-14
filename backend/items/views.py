from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all().order_by('-created_at')
    serializer_class = serializers.ItemSerializer


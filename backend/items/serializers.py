from . import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    #category_detail = CategorySerializer(source='category', read_only=True)
    class Meta:
        model = models.Item
        fields = "__all__"
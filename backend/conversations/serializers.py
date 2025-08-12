from rest_framework import serializers
from items.models import Item, Category
from . import models


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Conversations
        fields = "__all__"

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ConversationMessage
        fields = "__all__"
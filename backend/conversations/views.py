from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = models.Conversations.objects.all()
    serializer_class = serializers.ConversationSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = models.ConversationMessage.objects.all()
    serializer_class = serializers.MessageSerializer

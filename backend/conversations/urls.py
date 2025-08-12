from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'conversations', views.ConversationViewSet)
router.register(r'messages', views.MessagesViewSet)

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import path, include
from rest_framework import routers
from . import views

# app_name = "items"

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]

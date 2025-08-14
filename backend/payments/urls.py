from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'order', views.OrderViewSet)
router.register(r'payment', views.PaymentViewSet)
router.register(r'shipping', views.ShippingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

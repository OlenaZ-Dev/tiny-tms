from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ShipmentViewSet, TrackingEventViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'events', TrackingEventViewSet)

urlpatterns = [ path('', include(router.urls)), ]
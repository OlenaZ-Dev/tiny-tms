from rest_framework import serializers
from .models import Customer, Shipment, TrackingEvent

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    class Meta:
        model = Customer
        fields = ['id', 'name']
        read_only_fields = ['id']


class TrackingEventSerializer(serializers.ModelSerializer):
    """Serializer for TrackingEvent model."""
    class Meta:
        model = TrackingEvent
        fields = ['id', 'ts', 'status', 'comment', 'lat', 'lon', 'created_at']
        read_only_fields = ['id', 'created_at']


class ShipmentSerializer(serializers.ModelSerializer):
    """Serializer for Shipment model with embedded customer data."""
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(source='customer', queryset=Customer.objects.all(), write_only=True)
    class Meta:
        model = Shipment
        fields = ['id','number','status','origin','destination','eta','customer','customer_id','created_at']
        read_only_fields = ['id', 'created_at']
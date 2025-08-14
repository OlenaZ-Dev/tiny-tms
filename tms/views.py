from rest_framework import viewsets, permissions, response, status, decorators
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from .models import Customer, TrackingEvent, Shipment
from .serializers import CustomerSerializer, ShipmentSerializer, TrackingEventSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['name']
    search_fields = ['name']


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing shipments.
    Supports listing, retrieving, creating, updating, and deleting shipments.
    Includes a nested `events` endpoint for tracking shipment status changes.
    """
    queryset = Shipment.objects.select_related('customer').all().order_by('created_at')
    serializer_class = ShipmentSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['status', 'customer', 'origin', 'destination']
    search_fields = ['number', 'origin', 'destination']
    ordering_fields = ['created_at', 'eta']

    @decorators.action(
        detail=True,
        methods=['get', 'post'],
        url_path='events',
        serializer_class=TrackingEventSerializer
    )
    def events(self, request, pk=None):
        """
        GET: Return all tracking events for this shipment.
        POST: Create a new tracking event for this shipment.
        """
        shipment = self.get_object()

        if request.method == "GET":
            return response.Response(
                TrackingEventSerializer(shipment.events.all(), many=True).data
            )

        # Copy request data to avoid mutating the original
        data = request.data.copy()

        # Convert timestamp from string to datetime if necessary
        if isinstance(data.get('ts'), str):
            event_datetime = parse_datetime(data['ts'])
            if event_datetime:
                data['ts'] = event_datetime

        # Default to current shipment status if not provided
        data['status'] = data.get('status', shipment.status)

        event_serializer = TrackingEventSerializer(data=data)
        if event_serializer.is_valid():
            event = event_serializer.save(shipment=shipment)

            # Update shipment status if it changed
            if event.status and event.status != shipment.status:
                shipment.status = event.status
                shipment.save(update_fields=['status'])

            return response.Response(
                TrackingEventSerializer(event).data,
                status=status.HTTP_201_CREATED
            )

        return response.Response(
            event_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def perform_create(self, serializer):
        """
        When a shipment is created, automatically create an initial tracking event.
        """
        shipment = serializer.save()
        TrackingEvent.objects.create(
            shipment=shipment,
            ts=timezone.now(),
            status=shipment.status,
            comment="Shipment created"
        )


class TrackingEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing tracking events.
    """
    queryset = TrackingEvent.objects.select_related('shipment', 'shipment__customer').all()
    serializer_class = TrackingEventSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['shipment', 'status']
    ordering_fields = ['ts', 'created_at']
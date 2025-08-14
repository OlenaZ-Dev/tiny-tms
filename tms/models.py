from django.db import models


class Customer(models.Model):
    """Represents a company or individual that sends or receives shipments."""
    name = models.CharField(max_length=120, unique=True)
    def __str__(self):
        return self.name

class Shipment(models.Model):
    """Represents a shipment (e.g., a delivery order) linked to a specific customer."""

    class Status(models.TextChoices):
        CREATED = 'CREATED', 'CREATED'
        IN_TRANSIT = 'IN_TRANSIT', 'IN_TRANSIT'
        DELIVERED = 'DELIVERED', 'DELIVERED'
        DELAYED = 'DELAYED', 'DELAYED'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipments', help_text="The customer who owns this shipment.")
    number = models.CharField(max_length=50, unique=True, help_text="Unique shipment tracking number.")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED, db_index=True, help_text="Current status of the shipment.")
    origin = models.CharField(max_length=120, help_text="Shipment origin city.")
    destination = models.CharField(max_length=120, help_text="Shipment destination city.")
    eta = models.DateTimeField(null=True, blank=True, help_text="Estimated time of arrival.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['status']), models.Index(fields=['customer', 'status'])]
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"

    def __str__(self):
        return f"{self.number} ({self.status})"


class TrackingEvent(models.Model):
    """
    Represents a status update (event) for a shipment.
    For example: 'IN_TRANSIT', 'DELIVERED', etc.
    """
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="events", help_text="The shipment this event is related to.")
    ts = models.DateTimeField(help_text="Date and time of the tracking event.")
    status = models.CharField(max_length=20, choices=Shipment.Status.choices)
    comment = models.CharField(max_length=255, blank=True, help_text="Optional comment for the event.")
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, help_text="Latitude.")
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text="Longitude.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ts']
        indexes = [models.Index(fields=['shipment', 'ts'])]
        verbose_name = "Tracking Event"
        verbose_name_plural = "Tracking Events"

    def __str__(self):
        return f"{self.shipment.number} @ {self.ts} → {self.status}"
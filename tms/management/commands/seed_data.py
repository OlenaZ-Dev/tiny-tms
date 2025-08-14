from django.core.management.base import BaseCommand
from django.utils import timezone
from random import choice, randint
from datetime import timedelta
from tms.models import Customer, Shipment, TrackingEvent

class Command(BaseCommand):
    help = "Create demo customers, shipments and events"
    def handle(self, *args, **options):
        customers = [Customer.objects.get_or_create(name=n)[0] for n in ["Acme","Baltic","NorthWind"]]
        origins = ["Gdańsk","Gdynia","Sopot","Warszawa","Poznań"]
        dests   = ["Berlin","Prague","Vilnius","Kraków","Łódź"]
        for i in range(20):
            c = choice(customers)
            sh, _ = Shipment.objects.get_or_create(
                number=f"SHP-{1000+i}",
                defaults=dict(customer=c, status=Shipment.Status.CREATED,
                              origin=choice(origins), destination=choice(dests),
                              eta=timezone.now()+timedelta(days=randint(1,4))))
            ts0 = timezone.now()-timedelta(days=randint(1,2))
            sts = [Shipment.Status.CREATED, Shipment.Status.IN_TRANSIT, choice([Shipment.Status.DELIVERED, Shipment.Status.DELAYED])]
            for j, st in enumerate(sts):
                TrackingEvent.objects.get_or_create(
                    shipment=sh, ts=ts0+timedelta(hours=12*j), status=st, defaults=dict(comment=f"Auto {j}"))
            sh.status = sts[-1]; sh.save(update_fields=['status'])
        self.stdout.write(self.style.SUCCESS("Demo data created."))
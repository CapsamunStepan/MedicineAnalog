from django.core.management.base import BaseCommand

from meds.models import Medicine
from meds.services import extract_active_ingredient


class Command(BaseCommand):
    help = "Backfill active_ingredient for medicines."

    def add_arguments(self, parser):
        parser.add_argument(
            "--pharmacy",
            type=str,
            required=False,
            help="Filtru după farmacie (opțional)",
        )
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Rescrie active_ingredient chiar dacă este deja completat",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Limitează numărul de actualizări (0 = fără limită)",
        )

    def handle(self, *args, **kwargs):
        pharmacy = kwargs.get("pharmacy")
        overwrite = bool(kwargs.get("overwrite"))
        limit = int(kwargs.get("limit") or 0)

        qs = Medicine.objects.all().order_by("id")
        if pharmacy:
            qs = qs.filter(pharmacy=pharmacy)

        updated = 0
        for med in qs.iterator(chunk_size=200):
            if med.active_ingredient and not overwrite:
                continue
            med.active_ingredient = extract_active_ingredient(med.title)
            med.save(update_fields=["active_ingredient"])
            updated += 1
            if limit and updated >= limit:
                break

        self.stdout.write(self.style.SUCCESS(f"Updated {updated} medicines"))

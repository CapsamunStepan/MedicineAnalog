from django.core.management.base import BaseCommand
from meds.models import Medicine


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        count, _ = Medicine.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Таблица очищена, удалено {count} записей'))

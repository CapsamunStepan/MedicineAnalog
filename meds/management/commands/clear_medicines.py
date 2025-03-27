from django.core.management.base import BaseCommand
from meds.models import Medicine


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--pharmacy',
            type=str,
            help='Имя аптеки',
            required=True
        )

    def handle(self, *args, **kwargs):
        pharmacy = kwargs['pharmacy']
        count, _ = Medicine.objects.filter(pharmacy=pharmacy).delete()
        self.stdout.write(self.style.SUCCESS(f'Таблица очищена, удалено {count} записей'))

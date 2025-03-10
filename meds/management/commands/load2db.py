import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from meds.models import Medicine


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            help='Путь к JSON файлу с данными',
            required=True
        )
        parser.add_argument(
            '--pharmacy',
            type=str,
            help='Название аптеки',
            required=True
        )
        parser.add_argument(
            '--manufacturer',
            type=bool,
            default=False,
        )

    def handle(self, *args, **kwargs):
        json_path = os.path.join(settings.BASE_DIR, kwargs['path'])
        pharmacy = kwargs['pharmacy']
        manufacturer = kwargs['manufacturer']

        with open(json_path, 'r', encoding='utf-8') as file:
            products = json.load(file)

        if manufacturer:
            for product in products:
                Medicine.objects.create(
                    title=product['title'],
                    price=float(product['price'].replace(',', '')),
                    link=product['link'],
                    img=product['img'],
                    manufacturer=product['manufacturer'],
                    pharmacy=pharmacy,
                )
        else:
            for product in products:
                Medicine.objects.create(
                    title=product['title'],
                    price=float(product['price'].replace(',', '')),
                    link=product['link'],
                    img=product['img'],
                    pharmacy=pharmacy,
                )

import os
import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Fetch fresh data via Scrapy and load into DB."

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-scrapy",
            action="store_true",
            help="Не запускать Scrapy, только загрузить JSON в БД",
        )
        parser.add_argument(
            "--extract-active",
            action="store_true",
            help="Заполнить active_ingredient при загрузке/обновлении",
        )

    def handle(self, *args, **kwargs):
        skip_scrapy = bool(kwargs.get("skip_scrapy"))
        extract_active = bool(kwargs.get("extract_active"))

        base_dir = str(settings.BASE_DIR)
        scraper_dir = os.path.join(base_dir, "meds_scraper")

        outputs = {
            "apteka_md": os.path.join(scraper_dir, "apteka_md.json"),
            "farmacie_md": os.path.join(scraper_dir, "farmacie_md.json"),
            "farmacia_familiei": os.path.join(scraper_dir, "farmacia_familiei.json"),
            "hippocrates": os.path.join(scraper_dir, "hippocrates.json"),
        }

        if not skip_scrapy:
            for spider, out_path in outputs.items():
                self.stdout.write(f"Scraping {spider} ...")
                subprocess.run(
                    ["scrapy", "crawl", spider, "-O", out_path],
                    cwd=scraper_dir,
                    check=True,
                )

        # Reload DB for each pharmacy (simple MVP approach: clear and reimport)
        mapping = [
            ("apteka_md", "AptekaMD", True),
            ("farmacie_md", "FarmacieMD", False),
            ("farmacia_familiei", "FarmaciaFamiliei", True),
            ("hippocrates", "Hippocrates", True),
        ]

        for spider, pharmacy_name, has_manufacturer in mapping:
            json_path = outputs[spider]
            self.stdout.write(f"Reloading {pharmacy_name} from {json_path} ...")
            call_command("clear_medicines", pharmacy=pharmacy_name)
            call_command(
                "load2db",
                path=os.path.relpath(json_path, base_dir),
                pharmacy=pharmacy_name,
                manufacturer=has_manufacturer,
                extract_active=extract_active,
            )

        if extract_active:
            # Backfill in case some rows missed (e.g., empty titles)
            call_command("fill_active_ingredients")

        self.stdout.write(self.style.SUCCESS("Done"))

from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Medicine


class SearchViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.primary_medicine = Medicine.objects.create(
            title="Nurofen Forte",
            active_ingredient="Ibuprofen",
            price=Decimal("45.50"),
            link="https://example.com/nurofen",
            img="https://example.com/nurofen.png",
            manufacturer="Reckitt",
            pharmacy="Farmacia 1",
        )
        Medicine.objects.create(
            title="Ibuprofen Bios",
            active_ingredient="Ibuprofen",
            price=Decimal("22.10"),
            link="https://example.com/ibuprofen-bios",
            img="https://example.com/ibuprofen-bios.png",
            manufacturer="Bios",
            pharmacy="Farmacia 2",
        )
        cls.no_image_medicine = Medicine.objects.create(
            title="Paracetamol 500mg comp.",
            active_ingredient="Paracetamol",
            price=Decimal("8.35"),
            link="https://example.com/paracetamol",
            img="",
            manufacturer="Eurofarmaco SA",
            pharmacy="FarmaciaFamiliei",
        )

    def test_home_search_matches_title_and_active_ingredient(self):
        response = self.client.get(reverse("home"), {"query": "ibuprofen"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 2)

        titles = {medicine.title for medicine in response.context["all_medicines"]}
        self.assertEqual(titles, {"Nurofen Forte", "Ibuprofen Bios"})

    def test_suggest_returns_title_and_ingredient_matches(self):
        response = self.client.get(reverse("suggest"), {"q": "ibu"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()

        suggestion_texts = {item["text"] for item in payload["suggestions"]}
        suggestion_kinds = {item["kind"] for item in payload["suggestions"]}

        self.assertIn("Ibuprofen", suggestion_texts)
        self.assertIn("Ibuprofen Bios", suggestion_texts)
        self.assertIn("ingredient", suggestion_kinds)
        self.assertIn("title", suggestion_kinds)

    def test_medicine_detail_page_renders(self):
        response = self.client.get(reverse("medicine_detail", args=[self.primary_medicine.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MedicineAnalog")

    def test_analogs_page_renders(self):
        response = self.client.get(reverse("analogs"), {"ingredient": "Ibuprofen"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MedicineAnalog")

    def test_missing_image_uses_placeholder_on_detail_page(self):
        response = self.client.get(reverse("medicine_detail", args=[self.no_image_medicine.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/static/meds/img/medicine-placeholder.svg")

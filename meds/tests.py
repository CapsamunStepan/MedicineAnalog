from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse

from .models import Medicine, SearchQuery


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

    def _ensure_session_key(self):
        session = self.client.session
        session["history_seed"] = "1"
        session.save()
        return session.session_key

    def test_home_search_matches_title_and_active_ingredient(self):
        response = self.client.get(reverse("home"), {"query": "ibuprofen"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_count"], 2)
        self.assertContains(response, 'class="search-clear"')

        titles = {medicine.title for medicine in response.context["page_obj"].object_list}
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

    def test_suggest_recent_history_can_delete_single_item(self):
        session_key = self._ensure_session_key()
        SearchQuery.objects.create(
            query="paracetamol",
            query_norm="paracetamol",
            session_key=session_key,
        )
        SearchQuery.objects.create(
            query="vitamin c",
            query_norm="vitamin c",
            session_key=session_key,
        )

        response = self.client.post(reverse("delete_search_history_item"), {"query": "paracetamol"})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            SearchQuery.objects.filter(session_key=session_key, query_norm="paracetamol").exists()
        )
        self.assertTrue(
            SearchQuery.objects.filter(session_key=session_key, query_norm="vitamin c").exists()
        )
        self.assertEqual(response.json()["suggestions"], [{"text": "vitamin c", "kind": "recent"}])

    def test_suggest_recent_history_can_be_cleared(self):
        session_key = self._ensure_session_key()
        SearchQuery.objects.create(
            query="paracetamol",
            query_norm="paracetamol",
            session_key=session_key,
        )
        SearchQuery.objects.create(
            query="vitamin c",
            query_norm="vitamin c",
            session_key=session_key,
        )

        response = self.client.post(reverse("clear_search_history"))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(SearchQuery.objects.filter(session_key=session_key).exists())
        self.assertEqual(response.json()["suggestions"], [])

    def test_delete_history_endpoint_accepts_post_with_csrf_cookie_from_page(self):
        csrf_client = Client(enforce_csrf_checks=True)
        page_response = csrf_client.get(reverse("home"))
        csrf_token = page_response.cookies["csrftoken"].value

        session = csrf_client.session
        session["history_seed"] = "1"
        session.save()
        session_key = session.session_key

        SearchQuery.objects.create(
            query="paracetamol",
            query_norm="paracetamol",
            session_key=session_key,
        )

        response = csrf_client.post(
            reverse("delete_search_history_item"),
            {"query": "paracetamol"},
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            SearchQuery.objects.filter(session_key=session_key, query_norm="paracetamol").exists()
        )

    def test_language_switch_to_english_changes_home_ui(self):
        response = self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("home")},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search medicines and analogs")
        self.assertContains(response, "Search")
        self.assertEqual(self.client.session["language"], "en")

    def test_language_switch_to_russian_changes_home_ui(self):
        response = self.client.post(
            reverse("set_language"),
            {"language": "ru", "next": reverse("home")},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "\u041f\u043e\u0438\u0441\u043a \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432 \u0438 \u0430\u043d\u0430\u043b\u043e\u0433\u043e\u0432")
        self.assertContains(response, "\u041f\u043e\u0438\u0441\u043a")
        self.assertEqual(self.client.session["language"], "ru")

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

    def test_home_search_paginates_results_server_side(self):
        for idx in range(12):
            Medicine.objects.create(
                title=f"Paracetamol extra {idx}",
                active_ingredient="Paracetamol",
                price=Decimal("10.00") + Decimal(idx),
                link=f"https://example.com/paracetamol-{idx}",
                img="",
                manufacturer="Extra Pharma",
                pharmacy="FarmaciaFamiliei" if idx < 8 else "Hippocrates",
            )

        first_page = self.client.get(reverse("home"), {"query": "paracetamol"})
        second_page = self.client.get(reverse("home"), {"query": "paracetamol", "page": 2})

        self.assertEqual(first_page.status_code, 200)
        self.assertEqual(first_page.context["page_obj"].paginator.per_page, 10)
        self.assertEqual(len(first_page.context["page_obj"].object_list), 10)
        self.assertContains(first_page, 'class="medicine-card"', count=10)
        self.assertContains(first_page, "\u00cenainte")

        self.assertEqual(second_page.status_code, 200)
        self.assertEqual(second_page.context["page_obj"].number, 2)
        self.assertEqual(len(second_page.context["page_obj"].object_list), 3)
        self.assertContains(second_page, "\u00cenapoi")

    def test_home_search_shows_empty_state_when_nothing_found(self):
        response = self.client.get(reverse("home"), {"query": "zzznothingmatch"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Niciun rezultat")
        self.assertContains(response, "Nu am găsit nimic pentru")

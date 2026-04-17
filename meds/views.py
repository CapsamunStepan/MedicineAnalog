from django.core.paginator import Paginator
from django.db.models import Count, Min, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Medicine, SearchQuery


def _fmt_price(value):
    if value is None:
        return ""
    return f"{float(value):.2f}"


def _pagination_items(page_obj):
    total_pages = page_obj.paginator.num_pages
    current_page = page_obj.number

    if total_pages <= 7:
        return list(range(1, total_pages + 1))

    items = [1]
    start = max(2, current_page - 1)
    end = min(total_pages - 1, current_page + 1)

    if start > 2:
        items.append(None)

    items.extend(range(start, end + 1))

    if end < total_pages - 1:
        items.append(None)

    items.append(total_pages)
    return items


def home(request):
    query = request.GET.get("query", "")
    active_pharmacy = (request.GET.get("pharmacy") or "all").strip() or "all"
    page_number = request.GET.get("page") or "1"

    analogs = []
    landing = {}
    total_count = 0
    pharmacy_tabs = []
    page_obj = None

    if query:
        medicines = (
            Medicine.objects.filter(
                Q(title__icontains=query) | Q(active_ingredient__icontains=query)
            )
            .order_by("price", "id")
        )
        total_count = medicines.count()

        if not request.session.session_key:
            request.session.create()

        query_clean = query.strip()
        if query_clean and active_pharmacy == "all" and str(page_number) == "1":
            SearchQuery.objects.create(
                query=query_clean,
                query_norm=query_clean.lower(),
                mode=SearchQuery.MODE_TITLE,
                session_key=request.session.session_key or "",
            )

        if total_count:
            pharmacy_stats = list(
                medicines.values("pharmacy")
                .annotate(count=Count("id"), min_price=Min("price"))
                .order_by("-count", "min_price", "pharmacy")
            )

            available_pharmacies = {row["pharmacy"] for row in pharmacy_stats}
            if active_pharmacy != "all" and active_pharmacy not in available_pharmacies:
                active_pharmacy = "all"

            pharmacy_tabs = [
                {
                    "id": "all",
                    "label": "Toți",
                    "count": total_count,
                    "is_active": active_pharmacy == "all",
                }
            ]
            pharmacy_tabs.extend(
                {
                    "id": row["pharmacy"],
                    "label": row["pharmacy"],
                    "count": row["count"],
                    "is_active": row["pharmacy"] == active_pharmacy,
                }
                for row in pharmacy_stats
            )

            active_medicines = (
                medicines if active_pharmacy == "all" else medicines.filter(pharmacy=active_pharmacy)
            )
            page_obj = Paginator(active_medicines, 10).get_page(page_number)

            ingredients = (
                medicines.exclude(active_ingredient__isnull=True)
                .exclude(active_ingredient__exact="")
                .values("active_ingredient")
                .annotate(min_price=Min("price"))
                .order_by("min_price")[:10]
            )
            analogs = list(ingredients)
    else:
        total_medicines = Medicine.objects.count()
        total_pharmacies = Medicine.objects.values("pharmacy").distinct().count()
        popular_ingredients = list(
            Medicine.objects.exclude(active_ingredient__isnull=True)
            .exclude(active_ingredient__exact="")
            .values("active_ingredient")
            .annotate(cnt=Count("id"), min_price=Min("price"))
            .order_by("-cnt")[:8]
        )

        substance_count = (
            Medicine.objects.exclude(active_ingredient__isnull=True)
            .exclude(active_ingredient__exact="")
            .values("active_ingredient")
            .distinct()
            .count()
        )

        landing = {
            "total_medicines": total_medicines,
            "total_pharmacies": total_pharmacies,
            "popular_ingredients": popular_ingredients,
            "substance_count": substance_count,
        }

    return render(
        request,
        "meds/home.html",
        {
            "query": query,
            "active_pharmacy": active_pharmacy,
            "page_obj": page_obj,
            "pagination_items": _pagination_items(page_obj) if page_obj else [],
            "pharmacy_tabs": pharmacy_tabs,
            "analogs": analogs,
            "landing": landing,
            "total_count": total_count,
        },
    )


def medicine_detail(request, medicine_id: int):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    price_compare = []
    if medicine.active_ingredient:
        price_compare = list(
            Medicine.objects.filter(active_ingredient=medicine.active_ingredient)
            .values("pharmacy", "link")
            .annotate(min_price=Min("price"))
            .order_by("min_price")
        )

    cheap_analogs = []
    if medicine.active_ingredient:
        cheap_analogs = list(
            Medicine.objects.filter(active_ingredient=medicine.active_ingredient)
            .exclude(id=medicine.id)
            .order_by("price")[:5]
        )

    if len(cheap_analogs) < 5:
        existing_ids = {medicine.id} | {a.id for a in cheap_analogs}
        first_word = medicine.title.split()[0] if medicine.title else ""
        if first_word and len(first_word) >= 3:
            name_matches = (
                Medicine.objects.filter(title__istartswith=first_word)
                .exclude(id__in=existing_ids)
                .order_by("price")[: 5 - len(cheap_analogs)]
            )
            cheap_analogs.extend(name_matches)

    return render(
        request,
        "meds/medicine_detail.html",
        {
            "medicine": medicine,
            "price_compare": price_compare,
            "cheap_analogs": cheap_analogs,
        },
    )


def analogs(request):
    ingredient = request.GET.get("ingredient", "").strip()
    results = []

    if ingredient:
        qs = Medicine.objects.filter(active_ingredient__iexact=ingredient)
        results = list(
            qs.values("title", "manufacturer", "img")
            .annotate(min_price=Min("price"))
            .order_by("min_price")
        )

    return render(request, "meds/analogs.html", {"ingredient": ingredient, "results": results})


def suggest(request):
    q = (request.GET.get("q") or "").strip()

    if not q or len(q) < 2:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key or ""

        recents = []
        seen = set()
        if session_key:
            for row in (
                SearchQuery.objects.filter(session_key=session_key)
                .order_by("-created_at")
                .values("query")[:20]
            ):
                key = row["query"].strip().lower()
                if key in seen:
                    continue
                seen.add(key)
                recents.append({"text": row["query"], "kind": "recent"})
                if len(recents) >= 6:
                    break

        return JsonResponse({"suggestions": recents})

    suggestions = []

    ingredient_rows = (
        Medicine.objects.exclude(active_ingredient__isnull=True)
        .exclude(active_ingredient__exact="")
        .filter(active_ingredient__icontains=q)
        .values("active_ingredient")
        .annotate(cnt=Count("id"), min_price=Min("price"))
        .order_by("-cnt")[:6]
    )
    for row in ingredient_rows:
        suggestions.append(
            {
                "text": row["active_ingredient"],
                "kind": "ingredient",
                "count": row["cnt"],
                "min_price": _fmt_price(row["min_price"]),
            }
        )

    title_rows = (
        Medicine.objects.filter(title__icontains=q)
        .values("title")
        .annotate(cnt=Count("id"), min_price=Min("price"))
        .order_by("-cnt")[:6]
    )
    for row in title_rows:
        suggestions.append(
            {
                "text": row["title"],
                "kind": "title",
                "count": row["cnt"],
                "min_price": _fmt_price(row["min_price"]),
            }
        )

    seen = set()
    deduped = []
    for suggestion in suggestions:
        key = (suggestion.get("text") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        deduped.append(suggestion)

    return JsonResponse({"suggestions": deduped[:10]})

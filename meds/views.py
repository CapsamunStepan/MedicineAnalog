from django.db.models import Count, Min, Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Medicine, SearchQuery


def _fmt_price(value):
    if value is None:
        return ""
    return f"{float(value):.2f}"


def home(request):
    query = request.GET.get('query', '')
    mode = request.GET.get('mode', 'title')  # title | ingredient
    pharmacies = {}
    analogs = []
    landing = {}

    if query:
        # Persist search history (for landing: recent + top searches)
        if not request.session.session_key:
            request.session.create()

        query_clean = query.strip()
        if query_clean:
            SearchQuery.objects.create(
                query=query_clean,
                query_norm=query_clean.lower(),
                mode=mode if mode in (SearchQuery.MODE_TITLE, SearchQuery.MODE_INGREDIENT) else SearchQuery.MODE_TITLE,
                session_key=request.session.session_key or "",
            )

        medicines = Medicine.objects.filter(
            Q(title__icontains=query) | Q(active_ingredient__icontains=query)
        )

        # Группируем по аптеке
        for medicine in medicines:
            pharmacy = medicine.pharmacy
            if pharmacy not in pharmacies:
                pharmacies[pharmacy] = []
            pharmacies[pharmacy].append(medicine)

        for pharmacy, medicines_list in pharmacies.items():
            pharmacies[pharmacy] = sorted(medicines_list, key=lambda x: x.price)

        # Аналоги (если удалось выделить active_ingredient)
        ingredients = (
            medicines.exclude(active_ingredient__isnull=True)
            .exclude(active_ingredient__exact="")
            .values("active_ingredient")
            .annotate(min_price=Min("price"))
            .order_by("min_price")[:10]
        )
        analogs = list(ingredients)
    else:
        # Landing content when user hasn't searched yet
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

    all_medicines = sorted(
        [m for meds in pharmacies.values() for m in meds],
        key=lambda x: x.price,
    )

    return render(
        request,
        'meds/home.html',
        {
            'pharmacies': pharmacies,
            'query': query,
            'mode': mode,
            'analogs': analogs,
            'landing': landing,
            'total_count': len(all_medicines),
            'all_medicines': all_medicines,
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
    mode = request.GET.get("mode") or SearchQuery.MODE_TITLE
    mode = mode if mode in (SearchQuery.MODE_TITLE, SearchQuery.MODE_INGREDIENT) else SearchQuery.MODE_TITLE

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
                .values("query", "mode")[:20]
            ):
                key = row["query"].strip().lower()
                if key in seen:
                    continue
                seen.add(key)
                recents.append({"text": row["query"], "kind": "recent", "mode": row["mode"]})
                if len(recents) >= 6:
                    break

        return JsonResponse({"suggestions": recents})

    suggestions = []

    if mode == SearchQuery.MODE_INGREDIENT:
        med_rows = (
            Medicine.objects.exclude(active_ingredient__isnull=True)
            .exclude(active_ingredient__exact="")
            .filter(active_ingredient__icontains=q)
            .values("active_ingredient")
            .annotate(cnt=Count("id"), min_price=Min("price"))
            .order_by("-cnt")[:6]
        )
        for r in med_rows:
            suggestions.append(
                {
                    "text": r["active_ingredient"],
                    "kind": "ingredient",
                    "count": r["cnt"],
                    "min_price": _fmt_price(r["min_price"]),
                }
            )
    else:
        med_rows = (
            Medicine.objects.filter(title__icontains=q)
            .values("title")
            .annotate(cnt=Count("id"), min_price=Min("price"))
            .order_by("-cnt")[:6]
        )
        for r in med_rows:
            suggestions.append(
                {
                    "text": r["title"],
                    "kind": "title",
                    "count": r["cnt"],
                    "min_price": _fmt_price(r["min_price"]),
                }
            )

    seen = set()
    deduped = []
    for s in suggestions:
        key = (s.get("text") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        deduped.append(s)

    return JsonResponse({"suggestions": deduped[:10]})

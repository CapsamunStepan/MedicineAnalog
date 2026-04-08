from django.db.models import Count, Min
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Medicine, SearchQuery


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

        if mode == 'ingredient':
            medicines = Medicine.objects.filter(active_ingredient__icontains=query)
        else:
            medicines = Medicine.objects.filter(title__icontains=query)

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
            .order_by("-cnt")[:12]
        )

        session_key = request.session.session_key or ""
        recent_searches = []
        if session_key:
            recent_searches = list(
                SearchQuery.objects.filter(session_key=session_key)
                .order_by("-created_at")
                .values("query", "mode")[:8]
            )

        top_searches = list(
            SearchQuery.objects.values("query_norm", "mode")
            .annotate(cnt=Count("id"))
            .order_by("-cnt")[:12]
        )

        landing = {
            "total_medicines": total_medicines,
            "total_pharmacies": total_pharmacies,
            "popular_ingredients": popular_ingredients,
            "recent_searches": recent_searches,
            "top_searches": top_searches,
        }

    return render(
        request,
        'meds/home.html',
        {
            'pharmacies': pharmacies,
            'query': query,
            'mode': mode,
            'analogs': analogs,
            'landing': landing,
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

    return render(
        request,
        "meds/medicine_detail.html",
        {"medicine": medicine, "price_compare": price_compare},
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
    if not q or len(q) < 2:
        return JsonResponse({"suggestions": []})

    q_norm = q.lower()
    mode = mode if mode in (SearchQuery.MODE_TITLE, SearchQuery.MODE_INGREDIENT) else SearchQuery.MODE_TITLE

    suggestions = []

    # 1) From search history (top for prefix)
    for row in (
        SearchQuery.objects.filter(mode=mode, query_norm__startswith=q_norm)
        .values("query_norm")
        .annotate(cnt=Count("id"))
        .order_by("-cnt")[:6]
    ):
        suggestions.append({"text": row["query_norm"], "kind": "history", "count": row["cnt"]})

    # 2) From medicines (titles or active ingredients)
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
                    "min_price": str(r["min_price"]),
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
                    "min_price": str(r["min_price"]),
                }
            )

    # Deduplicate by text, keep first occurrence
    seen = set()
    deduped = []
    for s in suggestions:
        key = (s.get("text") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        deduped.append(s)

    return JsonResponse({"suggestions": deduped[:10]})

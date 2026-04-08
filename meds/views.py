from django.db.models import Min
from django.shortcuts import render, get_object_or_404
from .models import Medicine


def home(request):
    query = request.GET.get('query', '')
    mode = request.GET.get('mode', 'title')  # title | ingredient
    pharmacies = {}
    analogs = []

    if query:
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

    return render(
        request,
        'meds/home.html',
        {'pharmacies': pharmacies, 'query': query, 'mode': mode, 'analogs': analogs},
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

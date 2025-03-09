from django.shortcuts import render
from .models import Medicine


def home(request):
    query = request.GET.get('query', '')
    pharmacies = {}

    if query:
        medicines = Medicine.objects.filter(title__icontains=query)

        # Группируем по аптеке
        for medicine in medicines:
            pharmacy = medicine.pharmacy
            if pharmacy not in pharmacies:
                pharmacies[pharmacy] = []
            pharmacies[pharmacy].append(medicine)

        for pharmacy, medicines_list in pharmacies.items():
            pharmacies[pharmacy] = sorted(medicines_list, key=lambda x: x.price)

    return render(request, 'meds/home.html', {'pharmacies': pharmacies, 'query': query})



from django.shortcuts import render
from .models import Medicine


def home(request):
    query = request.GET.get('q')
    medicines = Medicine.objects.filter(name__icontains=query) if query else Medicine.objects.all()
    return render(request, 'meds/home.html', {'medicines': medicines})

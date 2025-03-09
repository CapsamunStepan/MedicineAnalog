from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'manufacturer', 'pharmacy')
    search_fields = ('title', 'manufacturer', 'pharmacy')
    list_filter = ('manufacturer', 'pharmacy')
    ordering = ('title',)

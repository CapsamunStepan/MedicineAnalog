from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('analogs/', views.analogs, name='analogs'),
    path('suggest/', views.suggest, name='suggest'),
    path('search-history/delete/', views.delete_search_history_item, name='delete_search_history_item'),
    path('search-history/clear/', views.clear_search_history, name='clear_search_history'),
    path('set-language/', views.set_language, name='set_language'),

]

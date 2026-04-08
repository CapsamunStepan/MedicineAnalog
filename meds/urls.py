from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('analogs/', views.analogs, name='analogs'),
    path('suggest/', views.suggest, name='suggest'),

]

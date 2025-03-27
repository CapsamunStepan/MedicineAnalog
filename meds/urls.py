from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<int:medicine_id>/', views.view_description, name='medicine_detail'),

]

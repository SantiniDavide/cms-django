from django.urls import path
from . import views

urlpatterns = [
    path('api/entries/', views.entry_list, name='entry_list'),  # già esistente
    path('', views.public_entry_list, name='public_entry_list'),
    path('entry/<int:pk>/', views.public_entry_detail, name='public_entry_detail'),
]

# billing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing, name='billing'),
    path('bill_summary/', views.bill_summary, name='bill_summary'),
]

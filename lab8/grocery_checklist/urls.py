# grocery_checklist/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page for the checklist
]

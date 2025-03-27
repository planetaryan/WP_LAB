# human_manager/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.human_manager, name='human_manager'),
]
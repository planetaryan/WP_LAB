# carinfo/urls.py
from django.urls import path
from . import views

app_name = 'carinfo' 

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]

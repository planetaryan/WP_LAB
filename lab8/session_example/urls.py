# session_example/urls.py
from django.urls import path
from . import views

app_name = 'session_example' 

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('second/', views.second_page, name='second_page'),
]

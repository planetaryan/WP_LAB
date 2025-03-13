# user_registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/<str:username>/<str:email>/<str:contact_number>/', views.success, name='success'),
]

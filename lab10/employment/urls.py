from django.urls import path
from . import views

urlpatterns = [
    path('add_works/', views.add_works, name='add_works'),
    path('add_lives/', views.add_lives, name='add_lives'),
    path('people_in_company/', views.people_in_company, name='people_in_company'),
]

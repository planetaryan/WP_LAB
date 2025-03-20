from django.urls import path
from . import views

urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/', views.add_page, name='add_page'),
    path('categories/', views.category_list, name='category_list'),
    path('pages/', views.page_list, name='page_list'),
]

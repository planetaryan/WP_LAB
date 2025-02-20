# my_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),
    path('frontcover/', include('frontcover.urls')),
    path('book/', include('book.urls')),
]

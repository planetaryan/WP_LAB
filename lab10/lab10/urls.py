from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directory/', include('directory.urls')),
    path('employment/', include('employment.urls')),
    path('institutes/', include('institutes.urls'))
]

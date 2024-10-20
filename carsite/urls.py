# carsite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('carapp.urls')),
    path('admin/', admin.site.urls),
]

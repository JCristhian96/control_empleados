"""
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.core.urls')),
    re_path('', include('applications.departamentos.urls')),
    re_path('', include('applications.empleados.urls')),
]

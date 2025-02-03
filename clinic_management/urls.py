# clinic_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('patients/', include('patients.urls')),
    path('appointments/', include('appointments.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('notes/', include('notes.urls')),
    path('reports/', include('reports.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

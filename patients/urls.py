# patients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),
    path('<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('<int:pk>/add_history/', views.add_medical_history, name='add_medical_history'),
    path('<int:pk>/upload_document/', views.upload_document, name='upload_document'),
]

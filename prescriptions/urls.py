# prescriptions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prescription_list, name='prescription_list'),
    path('create/', views.prescription_create, name='prescription_create'),
]

# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_report, name='practice_report'),
    path('graphs/', views.graphs, name='graphs'),
]

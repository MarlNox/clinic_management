# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.soapnote_list, name='soapnote_list'),
    path('create/', views.soapnote_create, name='soapnote_create'),
]

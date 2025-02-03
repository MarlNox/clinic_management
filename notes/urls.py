# notes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.soapnote_list, name='soapnote_list'),
    path('create/', views.soapnote_create, name='soapnote_create'),

    # New URL for ad hoc note creation
    path('ad-hoc/create/', views.ad_hoc_note_create, name='ad_hoc_note_create'),
]

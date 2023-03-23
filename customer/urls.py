# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('showings-by-date/', views.showings_by_date, name='showings_by_date'),
]

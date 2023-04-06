# urls.py
from django.urls import path
from .views.showings import showings_by_date, showing_details

urlpatterns = [
    path('showings-by-date/', showings_by_date, name='showings_by_date'),
    path('showing/<int:showing_id>/', showing_details, name='showing_details'),
]

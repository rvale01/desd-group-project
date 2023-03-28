# urls.py
from django.urls import path
from .views.showings import showings_by_date, showing_details
from .views.tickets import select_tickets, ticket_confirmation

urlpatterns = [
    path('showings-by-date/', showings_by_date, name='showings_by_date'),
    path('showing/<int:showing_id>/', showing_details, name='showing_details'),
]

urlpatterns += [
    path('select_tickets/<int:showing_id>/', select_tickets, name='select_tickets'),
    path('ticket_confirmation/<int:showing_id>/', ticket_confirmation, name='ticket_confirmation'),
]

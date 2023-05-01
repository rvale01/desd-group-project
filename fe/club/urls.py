# urls.py
from django.urls import path
from .views.general import homepage
from .views.showings import showings_by_date, showing_details
from .views.tickets import purchase_tickets, club_ticket_confirmation, success_page
from .views.bookings import booking_list
urlpatterns = [
    path('', homepage, name = 'club_homepage'),
]

urlpatterns += [
    path('showings-by-date/', showings_by_date, name='club_showings_by_date'),
    path('showing/<int:showing_id>/', showing_details, name='club_showing_details'),
]

urlpatterns += [
    path('select_tickets/<int:showing_id>/', purchase_tickets, name='club_select_tickets'),
    path('ticket_confirmation/', club_ticket_confirmation, name='club_ticket_confirmation'),
    path('success_page', success_page, name="success_page")
]

urlpatterns += [
    path('bookings/list', booking_list, name='booking_list'),
]
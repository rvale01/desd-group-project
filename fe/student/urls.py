# urls.py
from django.urls import path
from .views.showings import showing_details, showings_by_date
from .views.tickets import select_tickets, ticket_confirmation, handle_student_successful_payment
from django.urls import path

urlpatterns = [
    path('showings-by-date/', showings_by_date, name='student_showings_by_date'),
    path('showing/<int:showing_id>/', showing_details, name='student_showing_details'),
]

urlpatterns += [
    path('select_tickets/<int:showing_id>/', select_tickets, name='student_select_tickets'),
    path('ticket_confirmation/', ticket_confirmation, name='student_ticket_confirmation'),
    path('success/', handle_student_successful_payment, name="handle_student_successful_payment")
]

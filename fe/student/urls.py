# urls.py
from django.urls import path
from .views.general import homepage, student_booking_history
from .views.credit import success_top_up_student, add_credit_student
from .views.showings import showing_details, showings_by_date
from .views.tickets import select_tickets, ticket_confirmation
from .views.payment import handle_student_successful_payment
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

urlpatterns += [
    path('', homepage, name='student_homepage'),
    path('booking-history/', student_booking_history, name="student_booking_history"),
    path('top-up/success/', success_top_up_student, name='success_top_up_student'),
    path('top-up/form/', add_credit_student, name="add_credit_student")
]
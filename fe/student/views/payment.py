
from django.shortcuts import render
from cinemaManager.models.general import Booking, Showing
from django.contrib.auth.decorators import login_required
from student.models import Student

STUDENT_TICKET_PRICE = 8
@login_required
def handle_student_successful_payment(request):
    showing_id = request.session.get('showing_id')
    students_tickets = request.session.get('students_tickets')
    students_tickets = int(students_tickets) if students_tickets is not None else 0

    total_cost = students_tickets * STUDENT_TICKET_PRICE

    student = Student.objects.get(user=request.user)
    student.credit -= total_cost
    student.save()

    # Update the showing.available_seats
    showing = Showing.objects.get(showing_id=showing_id)
    showing.available_seats -= students_tickets
    showing.save()

    # Create the booking
    booking = Booking(
        customer=request.user,
        showing=showing,
        is_paid=False,
        students_tickets=students_tickets,
        clubs_tickets=0,
        total=total_cost
    )
    booking.save()
    return render(request, 'student/SuccessPage.html')

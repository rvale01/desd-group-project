from django.shortcuts import render
from cinemaManager.models.general import Booking, Showing
from django.contrib.auth.decorators import login_required
from customAuth.models.auth import StudentAccounts
from django.utils import timezone

# Define the student ticket price
STUDENT_TICKET_PRICE = 8

# Add the login_required decorator to restrict access to authenticated users only
@login_required
def handle_student_successful_payment(request):
    # Retrieve the showing_id from the session
    showing_id = request.session.get('showing_id')
    # Retrieve the students_tickets from the session
    students_tickets = request.session.get('students_tickets')
    # Ensure students_tickets is an integer or default to 0
    students_tickets = int(students_tickets) if students_tickets is not None else 0

    # Get the student object associated with the user
    student = StudentAccounts.objects.get(user=request.user)

    # Calculate the total cost of the booking
    total_cost = students_tickets * STUDENT_TICKET_PRICE
    total_cost = total_cost * (1-(student.discount/100))

    # Deduct the total cost from the student's balance and save the updated balance
    student.balance -= total_cost
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
        total=total_cost,
        booking_date = timezone.now().date()
    )
    booking.save()

    # Render the SuccessPage.html template
    return render(request, 'student/SuccessPage.html')

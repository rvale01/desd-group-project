from django.shortcuts import render
from cinemaManager.models.general import Booking, Showing, CinemaSettings
from django.contrib.auth.decorators import user_passes_test
from .general import restrict_to_student
from customAuth.models.auth import StudentAccounts
from django.utils import timezone

# Define the student ticket price
STUDENT_TICKET_PRICE = 8

# Define a function to assign ticket numbers based on total seats and booked seats,
# considering social distancing by leaving two spaces between each person
def assign_ticket_numbers(total_seats, booked_seats):
    # Initialize an empty list to store ticket numbers
    ticket_numbers = []
    # Set the initial seat number to the total number of seats
    seat_number = total_seats
    # Iterate through the range of booked seats
    for _ in range(booked_seats):
        # Add the current seat number to the ticket_numbers list
        ticket_numbers.append(seat_number)
        # Decrement the seat number by 3 (2 spaces for social distancing + 1 for the booked seat)
        seat_number -= (2 + 1)

    # Return the list of assigned ticket numbers
    return ticket_numbers


# Add the login_required decorator to restrict access to authenticated users only
@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def handle_student_successful_payment(request):
    # Retrieve the showing_id from the session
    showing_id = request.session.get('showing_id')
    # Retrieve the students_tickets from the session
    students_tickets = request.session.get('student_tickets')
    # Ensure students_tickets is an integer or default to 0
    students_tickets = int(students_tickets)

    # Get the student object associated with the user
    student = StudentAccounts.objects.get(user=request.user)

    # Calculate the total cost of the booking
    total_cost = students_tickets * STUDENT_TICKET_PRICE
    total_cost = total_cost * (1-(student.discount/100))

    # Deduct the total cost from the student's balance and save the updated balance
    student.balance -= total_cost
    student.save()

    social_distancing = CinemaSettings.objects.get(id=1).social_distancing

    # Update the showing.available_seats
    showing = Showing.objects.get(showing_id=showing_id)
    seats = []

    if social_distancing:
        seats = assign_ticket_numbers(showing.available_seats, students_tickets)
        showing.available_seats -= (students_tickets * 3) - 2
    else:
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
        booking_date = timezone.now().date(),
        reserved_seats=seats,
    )
    booking.save()

    # Render the SuccessPage.html template
    return render(request, 'student/SuccessPage.html')

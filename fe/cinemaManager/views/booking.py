from django.shortcuts import render, redirect
from ..models.general import Showing, Booking


def create_booking(request, showing_id):
    if request.method == 'POST':
        student_tickets = int(request.POST.get('students_tickets', 0))
        adult_tickets = int(request.POST.get('adults_tickets', 0))
        club_tickets = int(request.POST.get('clubs_tickets', 0))

        showing = Showing.objects.get(showing_id=showing_id)

        # Check if there are enough available seats
        total_tickets = student_tickets + adult_tickets + club_tickets
        if total_tickets > showing.available_seats:
           return (f"Sorry, there are only {showing.available_seats} seats available for this showing. Please reduce the number of tickets and try again.")

        # Calculate the total price for the booking (you can adjust the ticket prices as needed)
        total_price = student_tickets * 10 + adult_tickets * 15 + club_tickets * 12

        # Create the booking
        booking = Booking(showing=showing, is_paid=True, students_tickets=student_tickets, adults_tickets=adult_tickets, clubs_tickets=club_tickets, total=total_price)
        booking.save()

        # Update the available seats for the showing
        showing.available_seats -= total_tickets
        showing.save()

        return redirect('booking_success')  # Replace 'booking_success' with the name of the URL pattern for the booking success page

    return render(request, 'Bookings/create_booking.html', {'showing_id': showing_id})

def list_showings_booking(request):
    showings = Showing.objects.all()
    return render(request, 'Bookings/list_showings_booking.html', {'showings': showings})


def booking_success(request):
    return render(request, 'Bookings/booking_success.html')


from django.shortcuts import render
from cinemaManager.models.general import Booking, Showing



def handle_successful_payment(request, showing_id, adults_tickets, children_tickets, total_cost, response):
    # Update the showing.available_seats
    showing = Showing.objects.get(showing_id=showing_id)
    showing.available_seats -= (adults_tickets + children_tickets)
    showing.save()

    # Create the booking
    booking = Booking(
        customer=request.user,
        showing=showing,
        is_paid=True,
        students_tickets=0,
        clubs_tickets=0,
        adults_tickets=adults_tickets,
        children_tickets=children_tickets,
        total=total_cost
    )
    booking.save()
    return render(request, 'customer/SuccessPage.html')

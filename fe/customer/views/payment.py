
from django.shortcuts import render
from cinemaManager.models.general import Booking, Showing

ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

def handle_successful_payment(request):
    showing_id = request.session.get('showing_id')
    
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

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

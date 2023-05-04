
from django.shortcuts import render
from cinemaManager.models.general import GuestBooking, Showing

ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

def handle_successful_payment(request):
    showing_id = request.session.get('showing_id')
    
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')

    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    # Update the showing.available_seats
    showing = Showing.objects.get(showing_id=showing_id)
    showing.available_seats -= (adults_tickets + children_tickets)
    showing.save()

    # Create the booking
    booking = GuestBooking(
        customer_name=first_name,
        customer_lname=last_name,
        showing=showing,
        adults_tickets=adults_tickets,
        children_tickets=children_tickets,
        total=total_cost
    )
    booking.save()

    context = {
        'tickets_no': children_tickets + adults_tickets,
        'showing': showing
    }
    return render(request, 'customer/SuccessPage.html', context=context)

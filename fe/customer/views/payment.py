
from django.shortcuts import render
from cinemaManager.models.general import GuestBooking, Showing, CinemaSettings

ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

# Leaving just two spaces between each person
def assign_ticket_numbers(total_seats, booked_seats):
    # Assign ticket numbers to the seats
    ticket_numbers = []
    seat_number = total_seats
    for _ in range(booked_seats):
        ticket_numbers.append(seat_number)
        seat_number -= (2 + 1)

    return ticket_numbers


def handle_successful_payment(request):
    showing_id = request.session.get('showing_id')
    
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    total_booked_seats = adults_tickets + children_tickets
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')

    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    showing = Showing.objects.get(showing_id=showing_id)

    social_distancing = CinemaSettings.objects.get(id=1).social_distancing

    seats = []
    # Update the showing.available_seats based on the social distancing, if it's
    # on or off
    if(social_distancing):
        seats = assign_ticket_numbers(showing.available_seats, total_booked_seats)
        showing.available_seats -= (total_booked_seats * 3) - 2
    else:
        showing.available_seats -= total_booked_seats
    showing.save()


    # Create the booking
    booking = GuestBooking(
        customer_name=first_name,
        customer_lname=last_name,
        showing=showing,
        adults_tickets=adults_tickets,
        children_tickets=children_tickets,
        total=total_cost,
        reserved_seats=seats
    )
    booking.save()

    context = {
        'tickets_no': children_tickets + adults_tickets,
        'showing': showing,
        'seats': seats,
        "social_distancing": social_distancing
    }
    return render(request, 'customer/SuccessPage.html', context=context)

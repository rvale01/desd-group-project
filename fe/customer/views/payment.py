
from django.shortcuts import render
from cinemaManager.models.general import GuestBooking, Showing, CinemaSettings
from django.utils import timezone

# Define constants for adults and children ticket prices
ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

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

# Define a function to handle successful payment
def handle_successful_payment(request):
    # Retrieve and store showing_id, adults_tickets, and children_tickets from session
    showing_id = request.session.get('showing_id')
    
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    # Calculate the total number of booked seats
    total_booked_seats = adults_tickets + children_tickets
    # Retrieve and store first_name and last_name from session
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')

    # Calculate the total cost of the booking
    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    # Retrieve the showing object with the given showing_id
    showing = Showing.objects.get(showing_id=showing_id)

    # Retrieve the social distancing setting from CinemaSettings
    social_distancing = CinemaSettings.objects.get(id=1).social_distancing

    # Initialize an empty list to store seat numbers
    seats = []
    # Update the showing.available_seats based on the social distancing setting
    if(social_distancing):
        seats = assign_ticket_numbers(showing.available_seats, total_booked_seats)
        showing.available_seats -= (total_booked_seats * 3) - 2
    else:
        showing.available_seats -= total_booked_seats
    # Save the updated showing object
    showing.save()

    # Create a new GuestBooking object with the booking information
    booking = GuestBooking(
        customer_name=first_name,
        customer_lname=last_name,
        showing=showing,
        adults_tickets=adults_tickets,
        children_tickets=children_tickets,
        total=total_cost,
        reserved_seats=seats,
        booking_date = timezone.now().date()
    )
    # Save the new GuestBooking object
    booking.save()

    # Define the context for rendering the SuccessPage.html template
    context = {
        'tickets_no': children_tickets + adults_tickets,
        'showing': showing,
        'seats': seats,
        "social_distancing": social_distancing
    }
    # Render the SuccessPage

    return render(request, 'customer/SuccessPage.html', context=context)

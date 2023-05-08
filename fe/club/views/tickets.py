from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing, Booking, CinemaSettings
from customAuth.models.auth import Clubs
from ..forms.Tickets import CLubTicketPurchaseForm
from django.utils import timezone

CLUB_TICKET_PRICE = 10

def purchase_tickets(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    if request.method == 'POST':
        form = CLubTicketPurchaseForm(request.POST)
        if form.is_valid():
            request.session['num_tickets'] = form.cleaned_data['num_tickets']
            request.session['showing_id'] = showing_id
            return redirect('club_ticket_confirmation')
    
    form = CLubTicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
    }
    return render(request, 'ClubManager/SelectTickets.html', context)

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

def club_ticket_confirmation(request):
    club = Clubs.objects.get(club=request.user)
    showing_id = request.session.get('showing_id')
    showing = Showing.objects.get(showing_id=showing_id)
    num_tickets = request.session.get('num_tickets')
    
    total_cost = num_tickets * CLUB_TICKET_PRICE
    total_cost = total_cost * (1-(club.discount/100))

    social_distancing = CinemaSettings.objects.get(id=1).social_distancing

    seats = []
    if social_distancing:
        available_seats = showing.available_seats / 3
    else:
        available_seats = showing.available_seats
    
    error_message = ""
    if available_seats < num_tickets:
        return render(request, 'general/NoAvailability.html')
    if request.method == 'POST':
        
        if social_distancing:
            seats = assign_ticket_numbers(showing.available_seats, num_tickets)
            showing.available_seats -= (num_tickets * 3) - 2
        else:
            showing.available_seats = showing.available_seats - num_tickets
        
        club = Clubs.objects.get(club=request.user)
        if(club.balance >= total_cost):
            club.balance = club.balance-total_cost
            booking = Booking(
                customer=request.user, 
                showing = showing, 
                is_paid= False, 
                students_tickets=0, 
                clubs_tickets=num_tickets, 
                total=total_cost,
                booking_date = timezone.now().date(),
                reserved_seats = seats
            )
            showing.save()
            club.save()
            booking.save()
            return redirect('success_page')
        else:
            error_message = "Top up your account before the booking"
    context = {
        'total_cost': total_cost,
        'num_tickets': num_tickets,
        'discount': club.discount,
        'error': error_message
    }
    return render(request, 'ClubManager/TicketConfirmation.html', context)

def success_page(request):
    return render(request, 'ClubManager/SuccessPage.html')


from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing, Booking
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


def club_ticket_confirmation(request):
    club = Clubs.objects.get(club=request.user)
    showing_id = request.session.get('showing_id')
    showing = Showing.objects.get(showing_id=showing_id)
    num_tickets = request.session.get('num_tickets')
    
    total_cost = num_tickets * CLUB_TICKET_PRICE
    total_cost = total_cost * (1-(club.discount/100))

    available_seats = showing.available_seats
    
    error_message = ""
    if available_seats < num_tickets:
        return render(request, 'general/NoAvailability.html')
    if request.method == 'POST':
        showing.available_seats = showing.available_seats - num_tickets
        showing.save()
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
                booking_date = timezone.now().date()
            )
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


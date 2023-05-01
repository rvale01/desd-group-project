from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import TicketPurchaseForm
import requests
from cinemaManager.models.general import Showing, Booking
from django.contrib import messages

ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

def select_tickets(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            request.session['adults_tickets'] = form.cleaned_data['adults_tickets']
            request.session['children_tickets'] = form.cleaned_data['children_tickets']
            request.session['showing_id'] = showing_id
            return redirect('ticket_confirmation')

    form = TicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
    }
    return render(request, 'customer/SelectTickets.html', context)



def ticket_confirmation(request):
    showing_id = request.session.get('showing_id')

    showing = Showing.objects.get(showing_id=showing_id)
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    available_seats = showing.available_seats
    if available_seats < (adults_tickets + children_tickets):
        return render(request, 'customer/NoAvailability.html')
    if request.method == 'POST':
        response = requests.post(
            "http://services:8001/api/payment/create-tickets-session/",
            json={
                "adults_tickets": adults_tickets,
                "children_tickets": children_tickets,
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            
            
            showing.available_seats -= (adults_tickets + children_tickets)
            showing.save()

            
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

            
            return redirect(url)
        else:
            messages.error(request, "Payment failed. Please try again.")

    context = {'showing': showing, 'adults_tickets': adults_tickets, 'children_tickets': children_tickets, 'total_cost': total_cost}
    return render(request, 'customer/TicketConfirmation.html', context)
from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import TicketPurchaseForm

ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

def select_tickets(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            request.session['adults_tickets'] = form.cleaned_data['adults_tickets']
            request.session['children_tickets'] = form.cleaned_data['children_tickets']
            return redirect('ticket_confirmation', showing_id)
    else:
        form = TicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
    }
    return render(request, 'customer/SelectTickets.html', context)



def ticket_confirmation(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    adults_tickets = int(str(request.session.get('adults_tickets')))
    children_tickets = int(str(request.session.get('children_tickets')))

    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    available_seats = showing.available_seats
    if available_seats < (adults_tickets + children_tickets):
        return render(request, 'customer/NoAvailability.html')
    if request.method == 'POST':
        # TODO: add details about the stripe payment
        return redirect('stripe_payment')
    context = {'showing': showing, 'adults_tickets': adults_tickets, 'children_tickets': children_tickets, 'total_cost': total_cost}
    return render(request, 'customer/TicketConfirmation.html', context)

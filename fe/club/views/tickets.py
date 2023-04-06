from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import TicketPurchaseForm

STUDENT_TICKET_PRICE = 10

def purchase_tickets(request, showing_id):
    showing = Showing.objects.get(id=showing_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            request.session['num_tickets'] = form.cleaned_data['num_tickets']
            return redirect('ticket_confirmation')
    else:
        form = TicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
    }
    return render(request, 'ticket_purchase.html', context)



def ticket_confirmation(request, showing_id):
    showing = Showing.objects.get(id=showing_id)
    num_tickets = request.session.get('num_tickets')
    if num_tickets is None:
        return redirect('select_tickets', showing_id=showing_id)
    total_cost = num_tickets * STUDENT_TICKET_PRICE
    available_seats = showing.available_seats
    if available_seats < num_tickets:
        return render(request, 'customer/NoAvailability.html')
    if request.method == 'POST':
        # TODO: add details about the stripe payment
        return redirect('stripe_payment')
    else:
        form = TicketPurchaseForm()
    context = {'form': form, 'showing': showing, 'num_tickets': num_tickets, 'total_cost': total_cost}
    return render(request, 'general/NoAvailability.html', context)

from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import TicketPurchaseForm
import requests
from cinemaManager.models.general import Showing
from django.contrib import messages
from customer.views.payment import handle_successful_payment

# Define constants for adults and children ticket prices
ADULTS_TICKET_PRICE = 10
CHILDREN_TICKET_PRICE = 7

# Define a function to select tickets for a specific showing
def select_tickets(request, showing_id):
    # Retrieve the showing object with the given showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate the form with the data from the POST request
        form = TicketPurchaseForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Store the form data in the session
            request.session['adults_tickets'] = form.cleaned_data['adults_tickets']
            request.session['children_tickets'] = form.cleaned_data['children_tickets']
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            request.session['showing_id'] = showing_id
            # Redirect to the ticket_confirmation view
            return redirect('ticket_confirmation')

    form = TicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
    }
    return render(request, 'customer/SelectTickets.html', context)


# Define a function to confirm ticket purchase
def ticket_confirmation(request):
    # Retrieve the showing_id from the session
    showing_id = request.session.get('showing_id')

    # Retrieve the showing object with the given showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    # Retrieve the adults_tickets and children_tickets from the session
    adults_tickets = request.session.get('adults_tickets')
    adults_tickets = int(adults_tickets) if adults_tickets is not None else 0
    
    children_tickets = request.session.get('children_tickets')
    children_tickets = int(children_tickets) if children_tickets is not None else 0

    # Calculate the total cost of the booking
    total_cost = (adults_tickets) * (ADULTS_TICKET_PRICE)
    total_cost += (children_tickets) * (CHILDREN_TICKET_PRICE)

    # Check the availability of seats for the showing
    available_seats = showing.available_seats
    if available_seats < (adults_tickets + children_tickets):
        return render(request, 'customer/NoAvailability.html')

    # Check if the request method is POST
    if request.method == 'POST':
        # Send a POST request to create tickets session
        response = requests.post(
            "http://services:8001/api/payment/create-tickets-session/",
            json={
                "adults_tickets": adults_tickets,
                "children_tickets": children_tickets,
            },
        )

        # Redirect to the payment URL if the request was successful
        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)
        # Display an error

        else:
            messages.error(request, "Payment failed. Please try again.")
    # Define the context for rendering the TicketConfirmation.html template
    context = {'showing': showing, 'adults_tickets': adults_tickets, 'children_tickets': children_tickets, 'total_cost': total_cost}
     # Render the TicketConfirmation.html template with the given context
    return render(request, 'customer/TicketConfirmation.html', context)



    
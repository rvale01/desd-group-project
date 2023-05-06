from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import StudentTicketPurchaseForm
import requests
from cinemaManager.models.general import Showing
from django.contrib import messages
from student.views.payment import handle_student_successful_payment
from customAuth.models.auth import StudentAccounts
from django.contrib.auth.decorators import login_required

STUDENT_TICKET_PRICE = 8

# Decorate the select_tickets view with login_required to restrict access to authenticated users only
@login_required
def select_tickets(request, showing_id):
    # Get the showing object based on the provided showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    
    # Get the current logged-in student's account object
    student = StudentAccounts.objects.get(user=request.user)
    
    # Check if the request method is POST
    if request.method == 'POST':
        form = StudentTicketPurchaseForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Store the form data in the session
            request.session['student_tickets'] = form.cleaned_data['student_tickets']
            request.session['showing_id'] = showing_id
            # Redirect to the student_ticket_confirmation view
            return redirect('student_ticket_confirmation')

    # Initialize the form
    form = StudentTicketPurchaseForm()

    # Define the context for rendering the template
    context = {
        'showing': showing,
        'form': form,
        'student': student,
    }
    
    # Render the SelectTickets.html template with the context
    return render(request, 'student/SelectTickets.html', context)

# Decorate the ticket_confirmation view with login_required to restrict access to authenticated users only
@login_required
def ticket_confirmation(request):
    # Retrieve the showing_id from the session
    showing_id = request.session.get('showing_id')

    # Get the showing object based on the provided showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    
    # Retrieve the student_tickets from the session
    student_tickets = request.session.get('student_tickets')
    
    # Convert student_tickets to int if it's not None, otherwise set it to 0
    student_tickets = int(student_tickets) if student_tickets is not None else 0

    # Calculate the total cost for the student tickets
    total_cost = student_tickets * STUDENT_TICKET_PRICE

    # Check if there are enough available seats for the student_tickets
    available_seats = showing.available_seats
    if available_seats < student_tickets:
        # Render the NoAvailability.html template if there aren't enough seats
        return render(request, 'student/NoAvailability.html')
        
    # Check if the request method is POST
    if request.method == 'POST':
        # Redirect to the handle_student_successful_payment view
        return redirect('handle_student_successful_payment')

    # Define the context for rendering the TicketConfirmation.html template
    context = {
        'showing': showing,
        'student_tickets': student_tickets,
        'total_cost': total_cost
    }
    
    # Render the TicketConfirmation.html template with the context
    return render(request, 'student/TicketConfirmation.html', context)

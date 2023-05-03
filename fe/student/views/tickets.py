from django.shortcuts import render, redirect
from cinemaManager.models.general import Showing
from ..forms.Tickets import StudentTicketPurchaseForm
import requests
from cinemaManager.models.general import Showing
from django.contrib import messages
from student.views.payment import handle_student_successful_payment
from student.models import Student

from django.contrib.auth.decorators import login_required

STUDENT_TICKET_PRICE = 8

@login_required
def select_tickets(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        form = StudentTicketPurchaseForm(request.POST)
        if form.is_valid():
            top_up_credit = form.cleaned_data['top_up_credit']
            if top_up_credit:
                student.credit += top_up_credit
                student.save()
            
            request.session['students_tickets'] = form.cleaned_data['students_tickets']
            request.session['showing_id'] = showing_id
            return redirect('ticket_confirmation')

    form = StudentTicketPurchaseForm()

    context = {
        'showing': showing,
        'form': form,
        'student': student,
    }
    return render(request, 'student/SelectTickets.html', context)


@login_required
def ticket_confirmation(request):
    showing_id = request.session.get('showing_id')

    showing = Showing.objects.get(showing_id=showing_id)
    student_tickets = request.session.get('student_tickets')
    student_tickets = int(student_tickets) if student_tickets is not None else 0

    total_cost = student_tickets * STUDENT_TICKET_PRICE

    student = Student.objects.get(user=request.user)
    if student.credit < total_cost:
        messages.error(request, "Insufficient credit. Please top-up your account.")
        return redirect('select_tickets', showing_id=showing_id)

    available_seats = showing.available_seats
    if available_seats < student_tickets:
        return render(request, 'student/NoAvailability.html')
    if request.method == 'POST':
        response = requests.post(
            "http://services:8001/api/payment/create-tickets-session/",
            json={
                "student_tickets": student_tickets,
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)

        else:
            messages.error(request, "Payment failed. Please try again.")

    context = {'showing': showing, 'student_tickets': student_tickets, 'total_cost': total_cost}
    return render(request, 'student/TicketConfirmation.html', context)

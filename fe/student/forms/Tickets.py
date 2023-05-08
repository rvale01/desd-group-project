from django import forms

class StudentTicketPurchaseForm(forms.Form):
    # Define a form field for the number of student tickets to be purchased
    student_tickets = forms.IntegerField(min_value=1, label="Student Tickets")

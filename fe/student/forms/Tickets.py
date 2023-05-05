from django import forms

class StudentTicketPurchaseForm(forms.Form):
    student_tickets = forms.IntegerField(min_value=1, label="Student Tickets")
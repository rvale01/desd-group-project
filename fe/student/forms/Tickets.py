from django import forms

class StudentTicketPurchaseForm(forms.Form):
    student_tickets = forms.IntegerField(min_value=1, label="Student Tickets")
    top_up_credit = forms.DecimalField(min_value=0.01, max_digits=8, decimal_places=2, required=False, label='Top-up Credit (optional)')

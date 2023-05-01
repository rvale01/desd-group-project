from django import forms

class CLubTicketPurchaseForm(forms.Form):
    num_tickets = forms.IntegerField(min_value=10, label="Number of Tickets")
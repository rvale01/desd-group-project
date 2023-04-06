from django import forms

class TicketPurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=10, label="Number of Tickets")
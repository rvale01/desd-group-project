from django import forms

class TicketPurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Number of Tickets")
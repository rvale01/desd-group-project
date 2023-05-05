from django import forms

class TicketPurchaseForm(forms.Form):
    adults_tickets = forms.IntegerField(min_value=1, label="Adults")
    children_tickets = forms.IntegerField(min_value=0, label="Children")
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
from django import forms

# Define the TicketPurchaseForm class used during the booking process when there is a selection of the ticket
class TicketPurchaseForm(forms.Form):
    # Define an integer field for the number of adult tickets with a minimum value of 1 and a custom label
    adults_tickets = forms.IntegerField(min_value=1, label="Adults")
    # Define an integer field for the number of children tickets with a minimum value of 0 and a custom label
    children_tickets = forms.IntegerField(min_value=0, label="Children")
    # Define a character field for the customer's F name with a max of 100 characters
    first_name = forms.CharField(max_length=100)
    # Define a character field for the customer's L Name with a max of 100 characters
    last_name = forms.CharField(max_length=100)
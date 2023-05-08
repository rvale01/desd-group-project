# forms.py
from django import forms

# Define the DateSelectionForm class used during the booking process when the user selects the date
class DateSelectionForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        # Set the label for the date field
        label='Select a date'
    )

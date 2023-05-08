# forms.py
from django import forms

class DateSelectionForm(forms.Form):
    # Define a form field for selecting a date
    date = forms.DateField(
        
        widget=forms.DateInput(attrs={'type': 'date'}),
        # Set the label for the date field
        label='Select a date'
    )

# forms.py
from django import forms

# Define the DateSelectionForm class, which inherits from forms.Form
class DateSelectionForm(forms.Form):
    # Define the DateSelectionForm class, which inherits from forms.Form
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        # Set the label for the date field
        label='Select a date'
    )

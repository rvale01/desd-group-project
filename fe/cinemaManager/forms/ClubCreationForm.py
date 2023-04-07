
from customAuth.models.auth import Clubs
from django import forms

class ClubCreationForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ['club_name', 'rep_fname', 'rep_lname', 'street_no', 'city', 'mobile_phone', 'email']
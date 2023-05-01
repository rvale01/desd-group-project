
from customAuth.models.auth import Clubs
from django import forms
from django.contrib.auth.models import User, Group
import uuid

class ClubCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=100)
    class Meta:
        model = Clubs
        fields = ['club_name', 'rep_fname', 'rep_lname', 'street_no', 'city', 'mobile_phone', 'email', 'discount', 'balance']

        def save(self, commit=True):
            instance = super().save(commit=False)

            if(commit):
                instance.save()
            return instance
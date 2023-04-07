
from customAuth.models.auth import Clubs
from django import forms

class ClubCreationForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = "__all__"
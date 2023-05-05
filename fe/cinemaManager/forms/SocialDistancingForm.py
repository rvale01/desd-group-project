from django import forms
from ..models.general import CinemaSettings

class SocialDistancingForm(forms.ModelForm):
    class Meta:
        model = CinemaSettings
        fields = ['social_distancing']
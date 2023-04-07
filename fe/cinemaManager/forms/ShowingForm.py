from django import forms
from ..models.general import Showing, Film, Screen

class ShowingForm(forms.ModelForm):
    class Meta:
        model = Showing
        fields = '__all__'

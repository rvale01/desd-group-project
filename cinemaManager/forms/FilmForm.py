from django import forms
from ...group_14.models.general import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

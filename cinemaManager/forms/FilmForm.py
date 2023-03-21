from django import forms
from ..models.general import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'  
        labels = {
            'duration': 'Duration (in minutes):', 
        }

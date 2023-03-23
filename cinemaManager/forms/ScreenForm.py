from django import forms
from ..models.general import Screen

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = '__all__'  
        
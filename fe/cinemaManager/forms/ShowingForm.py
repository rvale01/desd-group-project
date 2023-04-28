from django import forms
from ..models.general import Showing, Film, Screen

class ShowingForm(forms.ModelForm):
    class Meta:
        model = Showing
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ShowingForm, self).__init__(*args, **kwargs)
        self.fields['film'].widget = forms.Select(choices=Film.objects.all().values_list('film_id', 'title'))
        self.fields['screen'].widget = forms.Select(choices=Screen.objects.all().values_list('screen_id', 'name'))


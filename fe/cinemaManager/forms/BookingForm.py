from django import forms
from ..models.general import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['showing', 'students_tickets', 'adults_tickets', 'clubs_tickets', 'is_paid', 'social_distancing']

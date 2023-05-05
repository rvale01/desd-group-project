
from customAuth.models.auth import Clubs
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ClubCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_phone = PhoneNumberField()
    class Meta:
        model = Clubs
        fields = ['club_name', 'rep_fname', 'rep_lname', 'street', 'street_no', 'city', 'mobile_phone', 'email', 'discount', 'balance']

        def save(self, commit=True):
            instance = super().save(commit=False)

            if(commit):
                instance.save()
            return instance
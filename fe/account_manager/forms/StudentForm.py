
from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from customAuth.models.auth import StudentAccounts
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_phone = PhoneNumberField()
    class Meta:
        model = StudentAccounts
        fields = ['balance', 'street', 'street_no', 'city', 'mobile_phone', 'email', 'discount', ]

    def __init__(self,*args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        
        instance = kwargs.get('instance')
        if instance and 'username' in instance.user:
            self.fields['username'].initial = instance.user.username
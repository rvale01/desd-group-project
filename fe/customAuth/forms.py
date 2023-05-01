from django import forms  
from django.contrib.auth.models import User, Group  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from .models.auth import StudentAccounts, Clubs

class CustomerCreationForm(UserCreationForm):  
    USER_TYPES = (
        ("student", "student"),
        # ("cinema_manager", "Cinema Manager"),
        # ("account_manager", "Account Manager"),
        ("club_manager", "Club"),
        ("customer", "Customer")
    )
    username = forms.CharField(label='username/Club Number', min_length=5, max_length=150)  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
    group = forms.ChoiceField(label='User Type', choices=USER_TYPES)
  
    # Checks if the username is already in the db, if it is, the form returns an error
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        user = User.objects.filter(username = username)  
        if user.count():  
            raise ValidationError("Ops! The username already is present in the database! Make sure to use a unique username")  
        return username  
  
    # Checks if both password are the same
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("The two passwords do not match! Try again, please!")  
        return password2  
  
    # On save of the form 
    def save(self):  
        selected_group = self.cleaned_data['group'].lower()
        # Getting the group of type customer
        customer_group, created = Group.objects.get_or_create(name=selected_group)
        # The user is created by using the username and password
        user = User.objects.create_user( 
            username= self.cleaned_data['username'],  
            password= self.cleaned_data['password1'],
        )  
        # The group is added to the user
        user.groups.add(customer_group)
        if(selected_group == "student"):
            # Create a new student account and associate it with the user
            student = StudentAccounts.objects.create(user=user)
            student.save()
        elif(selected_group == "club_manager"):
            club = Clubs(club=user)
            club.save()
        return user  
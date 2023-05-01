from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from customAuth.models.auth import Clubs
from django.shortcuts import render, redirect
from ..forms.AccountCreationForm import AccountCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
import uuid

def accounts_list(request):
    clubs = Clubs.objects.all()
    context = {'clubs': clubs}
    return render(request, 'AccountsDetails/AccountsList.html', context)

def add_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            club_name = form.cleaned_data['club_name']

            if Clubs.objects.filter(club_name=club_name).exists():
                form.add_error('club_name', 'A club with this name already exists.')
                return render(request, 'AccountsDetails/NewAccountForm.html', {'form': form})

            # Create a new user with a random password
            username = str(uuid.uuid4())
            password = User.objects.make_random_password()
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()

            # Add the new user to the 'ClubManager' group
            club_manager_group, created = Group.objects.get_or_create(name='club_manager')
            club_manager_group.user_set.add(new_user)

            # Save the club form with the new user as the club
            club = form.save(commit=False)
            club.club = new_user
            club.save()
            return redirect("accounts_list")
    else:
        form = AccountCreationForm()
    return render(request, 'AccountsDetails/NewAccountForm.html', {'form': form})


def update_account(request, club_id):
    club = Clubs.objects.get(id=club_id)

    if request.method == 'POST':
        form = AccountCreationForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('accounts_list')
    else:
        form = AccountCreationForm(instance=club)

    context = {'form': form}
    return render(request, 'AccountsDetails/UpdateAccountsDetails.html', context)

def delete_account(request, club_id):
    club_instance = Clubs.objects.get(id=club_id)
    club_instance.delete()
    return redirect('accounts_list')



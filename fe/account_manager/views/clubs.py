from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from customAuth.models.auth import Clubs
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from cinemaManager.forms.ClubCreationForm import ClubCreationForm
import uuid

def clubs_list_ac(request):
    clubs = Clubs.objects.all()
    context = {'clubs': clubs}
    return render(request, 'AccountManager/Clubs/ClubsList.html', context)

def add_club_account_ac(request):
    if request.method == 'POST':
        form = ClubCreationForm(request.POST)
        if form.is_valid():
            club_name = form.cleaned_data['club_name']

            if Clubs.objects.filter(club_name=club_name).exists():
                form.add_error('club_name', 'A club with this name already exists.')
                return render(request, 'AccountManager/Clubs/NewClub.html', {'form': form})

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
            return redirect("clubs_list_ac")
    else:
        form = ClubCreationForm()
    return render(request, 'AccountManager/Clubs/NewClub.html', {'form': form})


def update_club_account_ac(request, club_id):
    club = Clubs.objects.get(id=club_id)

    if request.method == 'POST':
        form = ClubCreationForm(request.POST, instance=club)
        if form.is_valid():

            user = User.objects.get(id=club.club.id)
            password = form.cleaned_data['password']

            if(password != ""):
                user.password = password
                user.save()
            form.save()
            return redirect('clubs_list_ac')
    else:
        form = ClubCreationForm(instance=club)

    context = {'form': form}
    return render(request, 'AccountManager/Clubs/UpdateClub.html', context)

def delete_club_account_ac(request, club_id):
    club_instance = Clubs.objects.get(id=club_id)
    if(club_instance.balance >= 0):
        club_instance.delete()
        return redirect('clubs_list_ac')
    else:
        error_message = "Cannot delete a club with a negative balance"
        return render(request, 'AccountManager/ErrorDeleteAccount.html', {'error_message': error_message})



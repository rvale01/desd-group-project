from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from customAuth.models.auth import Clubs

def restrict_to_club_managers(user):
    return user.groups.filter(name='club_manager').exists()

@user_passes_test(restrict_to_club_managers, login_url='/auth/accounts/login/')
def homepage(request):
    club = Clubs.objects.get(club=request.user)
    
    return render(request, 'ClubManager/Homepage.html', context={'balance': club.balance})   
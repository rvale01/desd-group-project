from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def restrict_to_cinema_managers(user):
    return user.groups.filter(name='cinemaManager').exists()

@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def homepage(request):
    return render(request, 'CinemaManager/Homepage.html')   

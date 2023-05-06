from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Define a test function to check if a user belongs to the 'cinema_manager' group
def restrict_to_cinema_managers(user):
    return user.groups.filter(name='cinema_manager').exists()

# Display the homepage for cinema managers, but only if the user belongs to the 'cinema_manager' group
@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def homepage(request):
    return render(request, 'CinemaManager/Homepage.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

# Function to handle user logout
def logoutView(request):
    logout(request)
    return redirect('home')
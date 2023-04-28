from django.shortcuts import redirect
from django.contrib.auth import logout

def logoutView(request):
    logout(request)
    return redirect('home')
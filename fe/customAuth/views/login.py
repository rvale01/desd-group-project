from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

# Function to redirect the user based on their group after logging in
def userRedirect(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='cinema_manager').exists():
            return redirect('/cinema-manager/')
        elif request.user.groups.filter(name='student').exists():
            return redirect('/students/')
        elif request.user.groups.filter(name='club_manager').exists():
            return redirect('/club/')
        elif request.user.groups.filter(name='account_manager').exists():
            return redirect('/account-manager/')
        
        
def customLogin(request):
    # If the request method is POST, handle form submission
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # If the user password and username are correct, the user var is not empty, therefore these lines of code log them in and redirect them
            if user is not None:
                login(request, user)
                return redirect('/auth/redirect-user/')
            else:
                form = AuthenticationForm()
                # If authentication failed, show an error message
                return render(request, 'registration/login.html', context={"form":form, 'error_message': 'Invalid username or password'})
        else:
            # If the form is not valid, show an error message
            form = AuthenticationForm()
            return render(request, 'registration/login.html', context={"form":form, 'error_message': 'Invalid username or password'})
    
    # If the request method is not POST, display the login form
    form = AuthenticationForm()
    return render(request, "registration/login.html", context={"form":form})
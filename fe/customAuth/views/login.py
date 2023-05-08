from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

def userRedirect(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='cinema_manager').exists():
            return redirect('/cinema-manager/')
        elif request.user.groups.filter(name='student').exists():
            return redirect('student')
        elif request.user.groups.filter(name='club_manager').exists():
            return redirect('/club/')
        elif request.user.groups.filter(name='account_manager').exists():
            return redirect('/account-manager/')
        
        
def customLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/auth/redirect-user/')
            else:
                return render(request, 'registration/login.html', context={'error_message': 'Invalid username or password'})
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', context={"form":form, 'error_message': 'Invalid username or password'})
    form = AuthenticationForm()
    return render(request, "registration/login.html", context={"form":form})

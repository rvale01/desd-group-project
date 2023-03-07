from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def customLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # FIXME: fix this by using the right redirect
                # if user.groups.filter(name='student').exists():
                #     return redirect('student_dashboard')
                # elif user.groups.filter(name='club').exists():
                #     return redirect('club_dashboard')
                # elif user.groups.filter(name='customer').exists():
                #     return redirect('customer_dashboard')
                # else:
                #     return redirect('home')
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'error_message': 'Invalid login credentials'})
    form = AuthenticationForm()
    return render(request=request, template_name="auth/login.html", context={"login_form":form})
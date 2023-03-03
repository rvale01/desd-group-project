from django.contrib.auth.models import User  
from django.shortcuts import render, redirect
from .forms import CustomerCreationForm
from django.contrib.auth import logout


# View to register a new customer 
def registrationCustomer(request):  
    form = CustomerCreationForm()  
    # If the user submits the form, this is saved, passed to the CustomerCreationForm and it's being checked if the form is valid
    if request.method == 'POST':  
        form = CustomerCreationForm(request.POST)  
        # if all the data in the form is correct/valid -> the form is saved -> data is saved in the db -> the user is redirected 
        # to the homepage
        if form.is_valid():  
            form.save()  
            return redirect('/accounts/login')
        
    # when the request.method is of type GET, the form is created and passed to the template
    return render(request, 'registration/registration.html', {
        'form':form  
    })  
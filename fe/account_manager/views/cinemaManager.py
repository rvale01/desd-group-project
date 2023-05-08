from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from ..forms.CinemaManagerForm import CinemaManagerForm

def cinema_managers_list_ac(request):
    group = Group.objects.get(name="cinema_manager")
    cinema_managers = group.user_set.all()

    context = {'cinema_managers': cinema_managers}
    return render(request, 'AccountManager/CinemaManagers/CinemaManagersList.html', context)

def new_cinema_manager_ac(request):  
    form = CinemaManagerForm()  
    # If the user submits the form, this is saved, passed to the CustomerCreationForm and it's being checked if the form is valid
    if request.method == 'POST':  
        form = CinemaManagerForm(request.POST)  
        # if all the data in the form is correct/valid -> the form is saved -> data is saved in the db -> the user is redirected 
        # to the homepage
        if form.is_valid():  
            form.save()  
            return redirect('cinema_managers_list_ac')
        
    # when the request.method is of type GET, the form is created and passed to the template
    return render(request, 'AccountManager/CinemaManagers/NewCinemaManager.html', {
        'form':form  
    })  

def delete_cinema_manager_account_ac(request, cinema_manager_id):
    cinema_manager_instance = User.objects.get(id=cinema_manager_id)
    cinema_manager_instance.delete()
    return redirect('cinema_managers_list_ac')
    


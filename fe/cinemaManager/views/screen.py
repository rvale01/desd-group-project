from django.shortcuts import render, redirect
from ..forms.ScreenForm import ScreenForm
from ..models.general import Screen, Showing
from django.contrib.auth.decorators import user_passes_test
from .general import restrict_to_cinema_managers

# Display the form to add a new screen

@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def addScreenForm(request):
    form = ScreenForm()
    if request.method == "GET":
        return render(request, 'Screens/AddScreen.html', {'form': form})  

# Add a new screen to the database
@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def addScreen(request):
    if request.method == "POST":
        form = ScreenForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to homepage
            return redirect('screenList')
        else:
            return render(request, 'Screens/AddScreen.html', {'form': form})  
    return redirect('screenList')    

# Edit a screen's details
@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def editScreen(request, screen_id):
    screen = Screen.objects.get(screen_id=screen_id)
    
    if request.method == 'POST':
        form = ScreenForm(request.POST, instance=screen)
        if form.is_valid():
            form.save()
            return redirect('screenList')
    else:
        form = ScreenForm(instance=screen)

    context = {'form': form, 'screen': screen}
    return render(request, 'Screens/EditScreen.html', context)

# Delete a screen from the database
@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def deleteScreen(request):
    if request.method == 'POST':
        screen_id = request.POST.get('screen_id')
        showings_no = Showing.objects.filter(screen_id=screen_id).count()

        if screen_id and showings_no == 0:
            Screen.objects.filter(screen_id=screen_id).delete()
            return redirect('screenList')
        else:
            screens = Screen.objects.all()
            context = {'screens': screens, 'error': 'Cannot delete screen, there are showings associated to it.'}
            return render(request, 'Screens/DeleteScreen.html',context)
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'Screens/DeleteScreen.html',context)

# List all screens
@user_passes_test(restrict_to_cinema_managers, login_url='/auth/accounts/login/')
def screenList(request):
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'Screens/ListScreens.html', context)

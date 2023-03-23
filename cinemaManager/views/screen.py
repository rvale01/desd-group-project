from django.shortcuts import render, redirect
from ..forms.ScreenForm import ScreenForm
from ..models.general import Screen

def addScreenForm(request):
    form = ScreenForm()
    if request.method == "GET":
        return render(request, 'Screens/AddScreen.html', {'form': form})  

def addScreen(request):
    if request.method == "POST":
        form = ScreenForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to homepage
            return redirect('screenList')
    return redirect('screenList')    

def screenList(request):
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'Screens/ListScreens.html', context)

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
        else:
            return render(request, 'Screens/AddScreen.html', {'form': form})  
    return redirect('screenList')    

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

def deleteScreen(request):
    if request.method == 'POST':
        screen_id = request.POST.get('screen_id')
        if screen_id:
            Screen.objects.filter(screen_id=screen_id).delete()
            return redirect('screenList')
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'Screens/DeleteScreen.html',context)

def screenList(request):
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'Screens/ListScreens.html', context)

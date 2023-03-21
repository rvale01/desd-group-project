from django.shortcuts import render, redirect
from ..forms.ShowingForm import ShowingForm
from ..models.general import Showing 

def addShowingForm(request):
    form = ShowingForm()
    if request.method == "GET":
        return render(request, 'Showings/AddShowing.html', {'form':form})

def addShowing(request):
    if request.method == "POST":
        form = ShowingForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('showingList')
    return redirect('showingList')

def deleteShowing(request):
    if request.method == 'POST':
        showing_id = request.POST.get('showing_id')
        if showing_id:
            Showing.objects.filter(id=showing_id).delete()
            return redirect('showingList')
    showings = Showing.objects.all()
    context = {'showings': showings}
    return render(request, 'Showings/DeleteShowing.html', context)

def showingList(request):
    showings = Showing.objects.all()
    context = {'showings': showings}
    return render(request, 'Showings/ListShowings.html', context)


def editShowing(request, showing_id):
    showing = Showing.objects.get(id=showing_id)

    if request.method == 'POST':
        form = ShowingForm(request.POST, instance=showing)
        if form.is_valid():
            form.save()
            return redirect('showingList')
    else:
        form = ShowingForm(instance=showing)

    context = {'form': form, 'showing': showing}
    return render(request, 'Showings/EditShowing.html', context)





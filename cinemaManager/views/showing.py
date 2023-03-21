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
            return redirect('home')
    return redirect('home')

def delete_showing(request, showing_id):
    if request.method == "POST":
        showing = Showing.objects.get(id = showing_id)
        showing.delete()
    return redirect('deleted_complete_view')
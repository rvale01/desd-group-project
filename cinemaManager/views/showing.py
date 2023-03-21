from django.shortcuts import render, redirect
from ..forms import ShowingForm
from ..models.general import Showing 

def addShowingForm(request):
    form = ShowingForm()
    if request.method == "GET":
        return render(request, 'Showings/AddShowing.html', {form:form})
    return redirect('home')

def addShowing(request):
    if request.method == "POST":
        form = ShowingForm(request.POST)
        if form.is_valid():
            # Get form data
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            age_rating = form.cleaned_data.get('age_rating')
            duration = form.cleaned_data.get('duration')
            
            # Create new Film object
            film = Film(title=title, description=description, age_rating=age_rating, duration=duration)
            
            # Save the new Film object to the database
            film.save()
            
            # Redirect to homepage
            return redirect('home')
    return redirect('home')


def addFilmForm(request):
    if request.method == "GET":
        return render(request, 'AddFilm.html')
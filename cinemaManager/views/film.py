from django.shortcuts import render, redirect
from ..forms.FilmForm import FilmForm
from ..models.general import Film 

def addFilmForm(request):
    form = FilmForm()
    if request.method == "GET":
        return render(request, 'Films/AddFilm.html', {'form': form})   

def addFilm(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to homepage
            return redirect('home')
    return redirect('home')

def delete_film(request, film_id):
    if request.method == "POST":
        film = Film.objects.get(id = film_id)
        film.delete()
    return redirect('deleted_complete_view')
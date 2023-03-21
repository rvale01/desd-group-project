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
            return redirect('film_list')
    return redirect('film_list')

def delete_film(request):
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        if film_id:
            Film.objects.filter(film_id=film_id).delete()
            return redirect('film_list')
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'Films/DeleteFilm.html', context)   

def film_list(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'Films/ListFilms.html', context)


def edit_film(request, film_id):
    film = Film.objects.get(film_id=film_id)
    
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm(instance=film)
    
    context = {'form': form, 'film': film}
    return render(request, 'Films/EditFilm.html', context)
from django.shortcuts import render, redirect
from ..forms.FilmForm import FilmForm
from ..models.general import Film, Showing
from django.contrib.auth.decorators import user_passes_test
from .general import restrict_to_cinema_managers

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def addFilmForm(request):
    form = FilmForm()
    if request.method == "GET":
        return render(request, 'Films/AddFilm.html', {'form': form})   

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def addFilm(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to homepage
            return redirect('filmList')
    return redirect('filmList')

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def deleteFilm(request):
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        if film_id:
            # Check if there are any showings associated with this film
            num_showings = Showing.objects.filter(film_id=film_id).count()
            if num_showings == 0:
                Film.objects.filter(film_id=film_id).delete()
                return redirect('filmList')
            else:
                # There are showings associated with this film, so don't delete it
                films = Film.objects.all()
                context = {'films': films, 'error': 'Cannot delete film, there are showings associated to it.'}
                return render(request, 'Films/DeleteFilm.html', context)
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'Films/DeleteFilm.html', context)

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def filmList(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'Films/ListFilms.html', context)

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def editFilm(request, film_id):
    film = Film.objects.get(film_id=film_id)
    
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('filmList')
    else:
        form = FilmForm(instance=film)
    
    context = {'form': form, 'film': film}
    return render(request, 'Films/EditFilm.html', context)


from django.shortcuts import render,redirect
from models import Film
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from models import Film
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from models import MyModel
from django.views.generic import ListView
from models import Film
from forms import FilmForm

class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('film_list')
    template_name = 'film_confirm_delete.html'

def delete_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    film.delete()
    return HttpResponseRedirect('/films/')

class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'

def create_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect('film_detail', pk=film.pk)
    else:
        form = FilmForm()
    return render(request, 'create_film.html', {'form': form})

def create_film(request):
    film = Film.create(
        title='THe Godfatherr',
        
        release_year=1998,
        genre='Action',
        description='a film about the Mafia.'
    )
    return HttpResponse(f'Created new film: {film.title}')

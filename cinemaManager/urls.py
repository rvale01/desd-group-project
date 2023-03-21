from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm, film_list, delete_film, edit_film
from .views.showing import addShowingForm, addShowing
from .views.general import homepage

urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
    path('films/', film_list, name='film_list'),
    path('delete/', delete_film, name='delete_film'),
    path('edit_film/<int:film_id>/', edit_film, name='edit_film'),
]

urlpatterns += [
    path('add-showing-form/', addShowingForm, name = 'addShowingForm'),
    path('add-new-showing/', addShowing, name = 'addShowing'),
]

urlpatterns += [
    path('', homepage, name = 'homepage'),
]
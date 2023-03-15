from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm
urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
]
from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm
from .views.showing import addShowingForm
urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
]

urlpatterns += [
    # path('add-showing-form/', addShowingForm, name = 'addShowingForm'),
]
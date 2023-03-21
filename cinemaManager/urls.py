from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm
from .views.showing import addShowingForm, addShowing
from .views.general import homepage

urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
]

urlpatterns += [
    path('add-showing-form/', addShowingForm, name = 'addShowingForm'),
    path('add-new-showing/', addShowing, name = 'addShowing'),
]

urlpatterns += [
    path('', homepage, name = 'homepage'),
]
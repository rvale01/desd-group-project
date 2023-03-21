from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm, filmList, deleteFilm, editFilm
from .views.showing import addShowingForm, addShowing
from .views.general import homepage

urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
    path('films/', filmList, name='filmList'),
    path('delete/', deleteFilm, name='deleteFilm'),
    path('editFilm/<int:film_id>/', editFilm, name='editFilm'),
]

urlpatterns += [
    path('add-showing-form/', addShowingForm, name = 'addShowingForm'),
    path('add-new-showing/', addShowing, name = 'addShowing'),
]

urlpatterns += [
    path('', homepage, name = 'homepage'),
]
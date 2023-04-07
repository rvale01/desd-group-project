from django.urls import path
from django.urls import path, include
from .views.film import addFilm, addFilmForm, filmList, deleteFilm, editFilm
from .views.screen import addScreenForm, addScreen, screenList, editScreen, deleteScreen
from .views.showing import addShowingForm, addShowing, showingList, deleteShowing, editShowing
from .views.general import homepage
from .views.clubs import clubs_list, add_club, delete_club, update_club

urlpatterns = []

urlpatterns += [
    path('add-film-form/', addFilmForm, name = 'addFilmForm'),
    path('add-new-film/', addFilm, name = 'addFilm'),
    path('films/', filmList, name='filmList'),
    path('films/delete/', deleteFilm, name='deleteFilm'),
    path('films/editFilm/<int:film_id>/', editFilm, name='editFilm'),
]

urlpatterns += [
    path('add-showing-form/', addShowingForm, name = 'addShowingForm'),
    path('add-new-showing/', addShowing, name = 'addShowing'),
    path('showings/', showingList, name='showingList'),
    path('showings/delete/', deleteShowing, name='deleteShowing'),
    path('showings/editShowing/<int:showing_id>/', editShowing, name='editShowing'),
]

urlpatterns += [
    path('add-screen-form/', addScreenForm, name = 'addScreenForm'),
    path('add-new-screen/', addScreen, name = 'addScreen'),
    path('screens/', screenList, name='screenList'),
    path('screens/editScreen/<int:screen_id>/', editScreen, name='editScreen'),
    path('screens/delete/', deleteScreen, name='deleteScreen'),
]

urlpatterns += [
    path('clubs/', clubs_list, name = 'clubs_list'),
    path('clubs/add-new', add_club, name = 'add_club'),
    path('clubs/edit/<int:club_id>', update_club, name = 'update_club'),
    path('clubs/delete/<int:club_id>', delete_club, name = 'delete_club'),
]

urlpatterns += [
    path('', homepage, name = 'homepage'),
]


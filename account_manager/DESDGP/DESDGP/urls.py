"""DESDGP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from cinema.views import film_list
from cinema.views import delete_film
from cinema.views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView

from . import views

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/delete/<int:film_id>/', delete_film, name='delete_film'),
    path('admin/', admin.site.urls),
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
]


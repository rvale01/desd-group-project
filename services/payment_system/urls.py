from django.urls import path

from .views import create_default_checkout_session

urlpatterns = [
    path('create-tickets-session/', create_default_checkout_session, name='create_default_checkout_session'),
    path('add-credit/')
]

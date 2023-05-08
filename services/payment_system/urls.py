from django.urls import path

from .views import create_default_checkout_session, add_credit

urlpatterns = [
    path('create-tickets-session/', create_default_checkout_session, name='create_default_checkout_session'),
    path('add-credit/', add_credit, name="add_credit")
]

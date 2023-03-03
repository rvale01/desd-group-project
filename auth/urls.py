from django.urls import path
from django.urls import path, include
from .views.registration import registrationCustomer

urlpatterns = []

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/customer', registrationCustomer, name = 'registrationCustomer'),
    # path('accounts/delete', views.delete_account),
]
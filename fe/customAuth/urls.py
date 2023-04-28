from django.urls import path
from django.urls import path, include
from .views.registration import registrationCustomer
from .views.login import customLogin
from .views.logout import logoutView


urlpatterns = []

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/customer', registrationCustomer, name = 'registrationCustomer'),
    path('login/', customLogin, name= 'customLogin'),
    path('logout/', logoutView, name='logout'),
    # path('accounts/delete', views.delete_account),
]
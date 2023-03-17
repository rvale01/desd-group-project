from django.urls import path
from django.urls import path, include
from .views.registration import registrationCustomer
from .views.login import customLogin
from .views.addScreen import addScreen


urlpatterns = []

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/customer', registrationCustomer, name = 'registrationCustomer'),
    path('login/', customLogin, name= 'customLogin'),
    path('addscreen/', addScreen, name='addScreen'),
    # path('accounts/delete', views.delete_account),
]
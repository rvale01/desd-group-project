from django.urls import path
from django.urls import path, include
from .views.registration import registrationCustomer
from .views.login import loginCustomer


urlpatterns = []

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/customer', registrationCustomer, name = 'registrationCustomer'),
    path('login/', loginCustomer, name= 'loginCustomer'),
    # path('accounts/delete', views.delete_account),
]
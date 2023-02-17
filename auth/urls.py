from django.urls import path
from django.urls import path, include

urlpatterns = []

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/delete', views.delete_account),
    # path('registration/', views.registrationCustomer, name = 'registrationCustomer'),
]
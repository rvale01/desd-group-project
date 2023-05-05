from django.urls import path
from django.urls import path, include
# from .views.general import homepage
from .views import accounts
from .views.accounts import accounts_list, add_account, delete_account, update_account

urlpatterns = []



urlpatterns += [
    path('accounts/', accounts.accounts_list, name = 'accounts_list'),
    path('accounts/add-new', accounts.add_account, name = 'add_account'),
    path('accounts/edit/<int:club_id>', accounts.update_account, name = 'update_account'),
    path('accounts/delete/<int:club_id>', accounts.delete_account, name = 'delete_account'),
]

# urlpatterns += [
#     path('', homepage, name = 'homepage'),
# ]


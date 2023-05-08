from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def restrict_to_account_managers(user):
    return user.groups.filter(name='account_manager').exists()

@user_passes_test(restrict_to_account_managers, login_url='/auth/accounts/login/')
def homepage(request):    
    return render(request, 'AccountManager/Homepage.html')   
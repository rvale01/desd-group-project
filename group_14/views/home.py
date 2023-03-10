from django.shortcuts import render, redirect

def homepage(request):
    # if user is logged out
    if not request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        # FIXME: redirect to other pages
        return None

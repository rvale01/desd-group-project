from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'CinemaManager/Homepage.html')   

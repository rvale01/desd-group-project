# from django.shortcuts import render, redirect
# from ..forms import FilmForm
# from group_14.models.general import Film 

# def addFilmForm(request):
#     if request.method == "GET":
#         return render(request, 'AddFilm.html')

# def addFilm(request):
#     if request.method == "POST":
#         form = FilmForm(request.POST)
#         if form.is_valid():
#             # Get form data
#             title = form.cleaned_data.get('title')
#             description = form.cleaned_data.get('description')
#             age_rating = form.cleaned_data.get('age_rating')
#             duration = form.cleaned_data.get('duration')
            
#             # Create new Film object
#             film = Film(title=title, description=description, age_rating=age_rating, duration=duration)
            
#             # Save the new Film object to the database
#             film.save()
            
#             # Redirect to homepage
#             return redirect('home')
#     return redirect('home')

# def delete_film(request, film_id):
#     if request.method == "POST":
#         film = Film.objects.get(id = film_id)
#         film.delete()
#     return redirect('deleted_complete_view')
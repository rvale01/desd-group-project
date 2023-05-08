from django.shortcuts import render
from ..forms.DateSelection import DateSelectionForm
from cinemaManager.models.general import Showing, CinemaSettings
from django.contrib.auth.decorators import user_passes_test
from .general import restrict_to_student

# Add the login_required decorator to restrict access to authenticated users only
@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def showings_by_date(request):
    # Initialize an empty list of showings
    showings = []
    # Create a DateSelectionForm instance
    form = DateSelectionForm()

    # Check if the request method is POST
    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Get the selected date from the form
            selected_date = form.cleaned_data['date']
            # Filter showings by the selected date
            showings = Showing.objects.filter(date=selected_date)

    # Define the context for rendering the template
    context = {'form': form, 'showings': showings}
    # Render the DateSelection.html template with the context
    return render(request, 'student/DateSelection.html', context)

# Add the login_required decorator to restrict access to authenticated users only
@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def showing_details(request, showing_id):
    # Get the showing object based on the provided showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    
    social_distancing = CinemaSettings.objects.get(id=1).social_distancing

    # Define the context for rendering the template
    context = {'showing': showing, 'social_distancing': social_distancing}
    # Render the ShowingDetails.html template with the context
    return render(request, 'student/ShowingDetails.html', context)

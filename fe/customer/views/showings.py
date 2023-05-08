# views.py
from django.shortcuts import render
from ..forms.DateSelection import DateSelectionForm
from cinemaManager.models.general import Showing

# Define a function to display showings by date
def showings_by_date(request):
    
    showings = []
    # Create an instance of DateSelectionForm
    form = DateSelectionForm()

    # Check if the request method is POST
    if request.method == 'POST':
        
        form = DateSelectionForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Retrieve the selected date from the form's cleaned data
            selected_date = form.cleaned_data['date']
            # Filter showings by the selected date
            showings = Showing.objects.filter(date=selected_date)

    # Define the context for rendering the DateSelection.html template
    context = {'form': form, 'showings': showings}
    # Render the DateSelection.html template with the given context
    return render(request, 'customer/DateSelection.html', context)

# Define a function to display showing details
def showing_details(request, showing_id):
    # Retrieve the showing object with the given showing_id
    showing = Showing.objects.get(showing_id=showing_id)
    # Define the context for rendering the ShowingDetails.html template
    context = {'showing': showing}
    # Render the ShowingDetails.html template with the given context
    return render(request, 'customer/ShowingDetails.html', context)
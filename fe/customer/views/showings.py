# views.py
from django.shortcuts import render
from ..forms.DateSelection import DateSelectionForm
from cinemaManager.models.general import Showing

def showings_by_date(request):
    showings = []
    form = DateSelectionForm()

    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date']
            showings = Showing.objects.filter(date=selected_date)

    context = {'form': form, 'showings': showings}
    return render(request, 'customer/DateSelection.html', context)

def showing_details(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)
    context = {'showing': showing}
    return render(request, 'customer/ShowingDetails.html', context)

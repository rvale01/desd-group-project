from django.shortcuts import render
from ..models.general import CinemaSettings
from ..forms.SocialDistancingForm import SocialDistancingForm
from django.http import HttpResponseRedirect

# View for updating cinema settings
def cinema_settings(request):
    cinema = CinemaSettings.objects.get(id=1)  # Get the cinema object

    # Handle the form submission for updating cinema settings
    if request.method == 'POST':
        form = SocialDistancingForm(request.POST, instance=cinema)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    # Display the form for updating cinema settings
    form = SocialDistancingForm(instance=cinema)
    return render(request, 'CinemaSettings/Cinema.html', {'form': form})
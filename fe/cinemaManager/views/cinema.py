from django.shortcuts import render
from ..models.general import CinemaSettings
from ..forms.SocialDistancingForm import SocialDistancingForm
from django.http import HttpResponseRedirect

def cinema_settings(request):
    cinema = CinemaSettings.objects.get(id=1)  # Get the cinema object

    if request.method == 'POST':
        form = SocialDistancingForm(request.POST, instance=cinema)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    form = SocialDistancingForm(instance=cinema)
    return render(request, 'CinemaSettings/Cinema.html', {'form': form})
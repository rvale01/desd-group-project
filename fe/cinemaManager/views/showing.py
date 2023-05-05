from django.shortcuts import render, redirect
from ..forms.ShowingForm import ShowingForm
from ..models.general import Showing, Booking, GuestBooking
from datetime import datetime, timedelta
from django.contrib.auth.decorators import user_passes_test
from .general import restrict_to_cinema_managers

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def addShowingForm(request):
    form = ShowingForm()
    if request.method == "GET":
        return render(request, 'Showings/AddShowing.html', {'form':form})
    
@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def addShowing(request):
    if request.method == "POST":
        form = ShowingForm(request.POST)
        if form.is_valid():
            showing = form.save(commit=False)
            screen = showing.screen
            available_seats = form.cleaned_data['available_seats']
            
            # Check if there are no other showings at the same screen on the same day and time
            date = showing.date
            start_time = showing.time
            end_time = (datetime.combine(date, start_time) + timedelta(minutes=showing.film.duration)).time()
            conflicting_showings = Showing.objects.filter(
                screen=screen, 
                date=date, 
                time__range=(start_time, end_time)
            ).exclude(showing_id=showing.showing_id)
            
            if conflicting_showings.exists():
                form.add_error(None, 'There is already a showing at this screen at the same date and time.')
                return render(request, 'Showings/AddShowing.html', {'form':form})
            
            if(screen.no_seats >= available_seats):
                showing.save()
                return redirect('showingList')
            else:
                form.add_error('available_seats', 'Not enough seats available.')
                return render(request, 'Showings/AddShowing.html', {'form':form})
    else:
        form = ShowingForm()
    return render(request, 'Showings/AddShowing.html', {'form':form})

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def deleteShowing(request):
    if request.method == 'POST':
        showing_id = request.POST.get('showing_id')
        num_showings = Booking.objects.filter(showing_id=showing_id).count()
        num_showings += GuestBooking.objects.filter(showing_id=showing_id).count()
        if showing_id and num_showings==0:
            Showing.objects.filter(showing_id=showing_id).delete()
            return redirect('showingList')
        else:
            showings = Showing.objects.all()
            context = {'showings': showings, 'error': 'Cannot delete the showing, there are bookings connected to it'}
            return render(request, 'Showings/DeleteShowing.html', context)

    showings = Showing.objects.all()
    context = {'showings': showings}
    return render(request, 'Showings/DeleteShowing.html', context)

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def showingList(request):
    showings = Showing.objects.all()
    context = {'showings': showings}
    return render(request, 'Showings/ListShowings.html', context)

@user_passes_test(restrict_to_cinema_managers,  login_url='/auth/accounts/login/')
def editShowing(request, showing_id):
    showing = Showing.objects.get(showing_id=showing_id)

    if request.method == 'POST':
        form = ShowingForm(request.POST, instance=showing)
        if form.is_valid():
            screen = showing.screen
            available_seats = form.cleaned_data['available_seats']

            date = showing.date
            start_time = showing.time
            end_time = (datetime.combine(date, start_time) + timedelta(minutes=showing.film.duration)).time()
            conflicting_showings = Showing.objects.filter(
                screen=screen, 
                date=date, 
                time__range=(start_time, end_time)
            ).exclude(showing_id=showing.showing_id)

            if conflicting_showings.exists():
                form.add_error(None, 'There is already a showing at this screen at the same date and time.')
                return render(request, 'Showings/EditShowing.html', {'form':form})
            
            if(screen.no_seats >= available_seats):
                showing.save()
                return redirect('showingList')
            else:
                form.add_error('available_seats', 'Not enough seats available.')
                return render(request, 'Showings/EditShowing.html', {'form':form})
    else:
        form = ShowingForm(instance=showing)

    context = {'form': form, 'showing': showing}
    return render(request, 'Showings/EditShowing.html', context)





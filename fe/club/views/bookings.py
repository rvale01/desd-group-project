from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cinemaManager.models.general import Booking

def booking_list(request):
    current_user = request.user
    bookings = Booking.objects.filter(user=current_user)

    return render(request, 'BookingList.html', {'bookings': bookings})

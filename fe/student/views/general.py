from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from cinemaManager.models.general import Booking
# function used to check if a user belongs to the 'cinema_manager' group
def restrict_to_student(user):
    return user.groups.filter(name='student').exists()

# Display the homepage for cinema managers, but only if the user belongs to the 'cinema_manager' group
@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def homepage(request):
    return render(request, 'student/Homepage.html')

@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def student_booking_history(request):
    customer = request.user

    bookings = Booking.objects.filter(customer = customer)

    return render(request, "student/BookingList.html",{'bookings': bookings})

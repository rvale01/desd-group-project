from django.db import models
from django.contrib.auth.models import User

class AdminAccounts(models.Model):
    ADMIN_USER_TYPES = (
        ('account_manager', 'Account Manager'),
        ('cinema_manager', 'Cinema Manager'),
    )
    type = models.CharField(max_length=20, choices=ADMIN_USER_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

class CustomerAccounts(models.Model):
    CUSTOMER_USER_TYPES = (
        ('student', 'student'),
        ('cinema_manager', 'Cinema Manager'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()
    user_type = models.CharField(max_length=20, choices=CUSTOMER_USER_TYPES)

class Clubs(models.Model):
    club = models.ForeignKey(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=100)
    rep_fname = models.CharField(max_length=100)
    rep_lname = models.CharField(max_length=100)
    rep_mobile = models.CharField(max_length=100)

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    age_rating = models.CharField(max_length=100)
    film_id = models.AutoField(primary_key=True)
    duration = models.IntegerField()

class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    no_seats = models.IntegerField(max = 300)

class Showing(models.Model):
    showing_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    available_seats = models.IntegerField()
    # Foreign key of type film
    film = models.ForeignKey(Film, to_field='film_id', on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, to_field='screen_id', on_delete=models.CASCADE)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=200)
    # Foreign key of type Showing
    showing = models.ForeignKey(Showing, to_field='showing_id', on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    students_tickets = models.IntegerField()
    adults_tickets = models.IntegerField()
    clubs_tickets = models.IntegerField()
    # reserved_seats = models. //TODO: has to be a list
    total = models.IntegerField()

from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
class Film(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    age_rating = models.CharField(max_length=100, default='Not Rated')
    film_id = models.AutoField(primary_key=True)
    duration = models.IntegerField()


class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    no_seats = models.IntegerField(validators=[MaxValueValidator(300)], default=0)


class Showing(models.Model):
    showing_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    available_seats = models.IntegerField()
    # Foreign key of type film
    film = models.ForeignKey(Film, to_field='film_id', on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, to_field='screen_id', on_delete=models.CASCADE, default=1)

# for logged in users -> students, clubs
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # Foreign key of type Showing
    showing = models.ForeignKey(Showing, to_field='showing_id', on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    students_tickets = models.IntegerField()
    clubs_tickets = models.IntegerField()
    reserved_seats = ArrayField(models.IntegerField(), blank=True, null=True)
    total = models.IntegerField()

# for not logged in users -> adults, children
class GuestBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_lname = models.CharField(max_length=100)
    # Foreign key of type Showing
    showing = models.ForeignKey(Showing, to_field='showing_id', on_delete=models.CASCADE)
    adults_tickets = models.IntegerField()
    children_tickets = models.IntegerField(default=0)
    reserved_seats = ArrayField(models.IntegerField(), blank=True, null=True)
    total = models.IntegerField()

class CinemaSettings(models.Model):
    social_distancing = models.BooleanField(default=False)
from django.db import models
from django.core.validators import MaxValueValidator

# TODO: MOVE THESE ONES IF NEEDED
class Screen(models.Model):
    class Meta:
        app_label = "Screen"
    screen_id = models.IntegerField(primary_key=True)
    no_seats = models.IntegerField(validators=[MaxValueValidator(300)])

class Film(models.Model):
    class Meta:
        app_label = "Film"
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    age_rating = models.CharField(max_length=100)
    film_id = models.AutoField(primary_key=True)
    duration = models.IntegerField()

class Showing(models.Model):
    class Meta:
        app_label = "Showing"
    showing_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    available_seats = models.IntegerField()
    # Foreign key of type film
    film = models.ForeignKey(Film, to_field='film_id', on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, to_field='screen_id', on_delete=models.CASCADE)

class Booking(models.Model):
    class Meta:
        app_label = "Booking"
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

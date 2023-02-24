from django.db import models
from django.contrib.auth.models import User

class AllUsers(models.Model):
    USER_TYPES = (
        ('student', 'student'),
        ('cinema_manager', 'Cinema Manager'),
        ('account_manager', 'Account Manager'),
        ('cinema_manager', 'Cinema Manager'),
    )
    type = models.CharField(max_length=20, choices=USER_TYPES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class StudentAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()

class Clubs(models.Model):
    balance = models.IntegerField()
    club = models.ForeignKey(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=100)
    rep_fname = models.CharField(max_length=100)
    rep_lname = models.CharField(max_length=100)
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()

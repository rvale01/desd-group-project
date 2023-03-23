from django.db import models
from django.contrib.auth.models import User

# This table includes all the students account and their details
class StudentAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()

# This table includes all the clubs accounts and their details
class Clubs(models.Model):
    balance = models.IntegerField(default=0)
    club = models.ForeignKey(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=100)
    rep_fname = models.CharField(max_length=100)
    rep_lname = models.CharField(max_length=100)
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()

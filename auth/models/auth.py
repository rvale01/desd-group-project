from django.db import models
from django.contrib.auth.models import User

# Table which includes all the users, the type is also specified for each user.
# Based on the type, the other appropriate table should be checked
class AllUsers(models.Model):
    USER_TYPES = (
        ("student", "student"),
        ("cinema_manager", "Cinema Manager"),
        ("account_manager", "Account Manager"),
        ("club", "Club"),
        ("customer", "Customer")
    )
    type = models.CharField(max_length=20, choices=USER_TYPES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# This table includes all the students account and their details
class StudentAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    street_no = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discount = models.IntegerField()

# This table includes all the clubs accounts and their details
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

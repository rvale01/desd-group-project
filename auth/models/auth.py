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
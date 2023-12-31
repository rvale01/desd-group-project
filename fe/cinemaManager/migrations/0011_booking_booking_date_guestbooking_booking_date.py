# Generated by Django 4.1.3 on 2023-05-08 01:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaManager', '0010_cinemasettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='guestbooking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

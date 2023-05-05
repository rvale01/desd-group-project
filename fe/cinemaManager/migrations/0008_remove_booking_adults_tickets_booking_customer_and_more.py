# Generated by Django 4.1.3 on 2023-05-01 13:55

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinemaManager', '0007_alter_showing_screen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='adults_tickets',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='reserved_seats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.CreateModel(
            name='GuestBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_lname', models.CharField(max_length=100)),
                ('adults_tickets', models.IntegerField()),
                ('reserved_seats', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('total', models.IntegerField()),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemaManager.showing')),
            ],
        ),
    ]
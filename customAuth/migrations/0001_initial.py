# Generated by Django 4.1.3 on 2023-03-21 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('street_no', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('club_name', models.CharField(max_length=100)),
                ('rep_fname', models.CharField(max_length=100)),
                ('rep_lname', models.CharField(max_length=100)),
                ('street_no', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
from django.shortcuts import render, redirect
from customAuth.models.auth import Clubs
import requests

CLUB_TICKET_PRICE = 10

def add_credit(request):
    if(request.method == "POST"):
        response = requests.post(
            "http://services:8001/api/payment/add-credit-club/",
            json={
                "username": request.user.username,
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)
        else:
            pass

    club = Clubs.objects.get(club=request.user)
    context = {
        "credit": club.balance
    }
    return render(request, "ClubManager/AddCredit.html", context=context)
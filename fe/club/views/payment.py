from django.shortcuts import render, redirect
from customAuth.models.auth import Clubs
import requests

def add_credit_club(request):
    if(request.method == "POST"):
        request.session['amount'] = request.POST.get('amount')
        response = requests.post(
            "http://services:8001/api/payment/add-credit/",
            json={
                "username": request.user.username,
                "amount": request.POST.get('amount'),
                "url": "club/top-up/success/"
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)
        else:
            pass

    return render(request, "ClubManager/AddCredit.html")

def success_top_up_club(request):
    club = Clubs.objects.get(club=request.user)

    amount = request.session.get('amount')
    club.balance += int(amount)
    club.save()
    return redirect('student_homepage') 

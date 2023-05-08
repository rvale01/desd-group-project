# student/views/credit.py
from customAuth.models.auth import StudentAccounts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests

# Add the login_required decorator to restrict access to authenticated users only
@login_required
def success_top_up_student(request):
    # Get the student object associated with the user
    student = StudentAccounts.objects.get(user=request.user)

    # Retrieve the amount to be added to the student's credit from the submitted form
    amount = int(request.POST.get('amount'))
    # Add the amount to the student's credit
    student.credit += amount
    # Save the updated student object
    student.save()
    # Redirect the user to the SuccessPage
    return redirect('student_homepage') 


def add_credit_student(request):
    if(request.method == "POST"):
        response = requests.post(
            "http://services:8001/api/payment/add-credit/",
            json={
                "username": request.user.username,
                "amount": request.POST.get('amount'), 
                "success_url": "students/top-up/success/"
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)
        else:
            pass

    return render(request, "student/AddCredit.html")

# student/views/credit.py
from customAuth.models.auth import StudentAccounts
from django.shortcuts import render, redirect
from .general import restrict_to_student
from django.contrib.auth.decorators import user_passes_test
import requests

# Add the login_required decorator to restrict access to authenticated users only
@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def success_top_up_student(request):
    # Get the student object associated with the user
    student = StudentAccounts.objects.get(user=request.user)

    # Retrieve the amount to be added to the student's credit from the submitted form
    amount = request.session.get('amount')
    # Add the amount to the student's credit
    student.balance += int(amount)
    # Save the updated student object
    student.save()
    # Redirect the user to the SuccessPage
    return redirect('student_homepage') 


@user_passes_test(restrict_to_student, login_url='/auth/accounts/login/')
def add_credit_student(request):
    if(request.method == "POST"):
        request.session['amount'] = request.POST.get('amount')
        response = requests.post(
            "http://services:8001/api/payment/add-credit/",
            json={
                "username": request.user.username,
                "amount": int(request.POST.get('amount')), 
                "url": "students/top-up/success/"
            },
        )

        if response.status_code == 200:
            url = response.json()["url"]
            return redirect(url)
        else:
            pass

    return render(request, "student/AddCredit.html")

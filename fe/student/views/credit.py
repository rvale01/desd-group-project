# student/views/credit.py
from student.apps import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Add the login_required decorator to restrict access to authenticated users only
@login_required
def top_up_student_credit(request):
    # Get the student object associated with the user
    student = Student.objects.get(user=request.user)

    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the amount to be added to the student's credit from the submitted form
        amount = int(request.POST.get('amount'))
        # Add the amount to the student's credit
        student.credit += amount
        # Save the updated student object
        student.save()
        # Redirect the user to the SuccessPage
        return redirect('SuccessPage') 

    # Prepare the context for rendering the template
    context = {
        'student': student
    }
    # Render the TopUpCredit.html template with the context
    return render(request, 'student/TopUpCredit.html', context)

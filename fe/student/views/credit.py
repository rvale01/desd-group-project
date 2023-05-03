# student/views/credit.py
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def top_up_student_credit(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        student.credit += amount
        student.save()
        return redirect('SuccessPage') 

    context = {
        'student': student
    }
    return render(request, 'student/TopUpCredit.html', context)

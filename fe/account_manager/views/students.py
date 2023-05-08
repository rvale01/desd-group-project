from customAuth.models.auth import StudentAccounts
from ..forms.StudentForm import StudentForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect


def students_list_ac(request):
    students = StudentAccounts.objects.all()
    context = {'students': students}
    return render(request, 'AccountManager/Students/StudentsList.html', context)

def add_student_account_ac(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            if StudentAccounts.objects.filter(user_username=username).exists():
                form.add_error('username', 'A student with this username already exists.')
                return render(request, 'AccountManager/Students/NewStudent.html', {'form': form})

            # Create a new user with a random password
            password = form.cleaned_data['password']
            new_user = StudentAccounts.objects.create_user(username=username, password=password)
            new_user.save()

            # Add the new user to the 'student' group
            student_group, created = Group.objects.get_or_create(name='student')
            student_group.user_set.add(new_user)

            # Save the student form with the new user as the student
            student = form.save(commit=False)
            student.user = new_user
            student.save()
            return redirect("students_list_ac")
    else:
        form = StudentForm()
    return render(request, 'AccountManager/Students/NewStudent.html', {'form': form})

def update_student_account_ac(request, student_id):
    student = StudentAccounts.objects.get(id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            user = User.objects.get(id=student.user.id)
            username = form.cleaned_data['username']
            user.username = username

            user.save()
            form.save()
            return redirect('students_list_ac')
    else:
        form = StudentForm(instance=student)

    context = {'form': form}
    return render(request, 'AccountManager/Students/UpdateStudent.html', context)

def delete_student_account_ac(request, student_id):
    student_instance = StudentAccounts.objects.get(id=student_id)
    if(student_instance.balance > 0):
        student_instance.delete()
        return redirect('students_list_ac')
    else:
        error_message = "Cannot delete a student with a negative balance"
        return render(request, 'AccountManager/ErrorDeleteAccount.html', {'error_message': error_message})
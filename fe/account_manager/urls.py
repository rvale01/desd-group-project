from django.urls import path
from django.urls import path, include
from .views.general import homepage
from .views.clubs import clubs_list_ac, add_club_account_ac, update_club_account_ac, delete_club_account_ac
from .views.students import students_list_ac, add_student_account_ac, delete_student_account_ac, update_student_account_ac
from .views.cinemaManager import cinema_managers_list_ac, delete_cinema_manager_account_ac, new_cinema_manager_ac
urlpatterns = []

urlpatterns += [
    path('', homepage, name = 'account_manager_homepage'),
]

urlpatterns += [
    path('accounts/clubs', clubs_list_ac, name = 'clubs_list_ac'),
    path('accounts/clubs/add-new', add_club_account_ac, name = 'add_club_account_ac'),
    path('accounts/clubs/edit/<int:club_id>', update_club_account_ac, name = 'update_club_account_ac'),
    path('accounts/clubs/delete/<int:club_id>', delete_club_account_ac, name = 'delete_club_account_ac'),
]

urlpatterns += [
    path('accounts/cinema-managers', cinema_managers_list_ac, name = 'cinema_managers_list_ac'),
    path('accounts/cinema-managers/add-new', new_cinema_manager_ac, name = 'new_cinema_manager_ac'),
    path('accounts/cinema-managers/delete/<int:cinema_manager_id>', delete_cinema_manager_account_ac, name = 'delete_cinema_manager_account_ac'),
]

urlpatterns += [
    path('accounts/students', students_list_ac, name = 'students_list_ac'),
    path('accounts/students/add-new', add_student_account_ac, name = 'add_student_account_ac'),
    path('accounts/students/edit/<int:student_id>', update_student_account_ac, name = 'update_student_account_ac'),
    path('accounts/students/delete/<int:student_id>', delete_student_account_ac, name = 'delete_student_account_ac'),
]

# FIXME: do this page
# urlpatterns += [
#     path('bookings/list')
# ]
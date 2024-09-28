from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from upis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('manage_subjects/', views.manage_subjects, name='manage_subjects'),
    path('subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('student_list/', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('professor/<int:professor_id>/', views.edit_professor, name='edit_professor'),
    path('professor_list/', views.professor_list, name='professor_list'),
    path('add_professor/', views.add_professor, name='add_professor'),
    path('students/<int:student_id>/upisni_list/', views.edit_student_upisni_list, name='edit_student_upisni_list'),
    path('students/<int:student_id>/upisni_list/remove/<int:predmet_id>/', views.remove_predmet_from_upisni_list, name='remove_predmet_from_upisni_list'),
    path('upisni_list//<int:predmet_id>/', views.show_upisni_list, name='show_upisni_list'),
    path('upisni_list/', views.student_upisni_list, name='student_upisni_list'),
    path('predmeti/', views.professor_subjects, name='professor_subjects'),
    path('predmeti/<int:predmet_id>/', views.predmet_details, name='predmet_details'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('studenti_10_ects/', views.studenti_10_ects, name='studenti_10_ects'),
    
]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F
from .forms import * 
from .models import *

# Universal
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            uloga = form.cleaned_data['uloga']
            try:
                Korisnik.objects.create_user(username=username, email=email, password=password, uloga=uloga)
                return redirect('login')
            except Exception as e:
                print(f"Error creating user: {e}")
                form.add_error(None, "There was an error creating the user.")
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Neispravno korisnicko ime ili lozinka'})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    user_role = request.user.uloga.naziv
    return render(request, 'home.html', {'user_role': user_role})

# Admin
@login_required
def manage_subjects(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')
    
    subjects = Predmet.objects.all()
    return render(request, 'manage_subjects.html', {'subjects': subjects})


@login_required
def edit_subject(request, subject_id):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')
    
    subject = get_object_or_404(Predmet, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('manage_subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form})


@login_required
def add_subject(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_subjects')
    else:
        form = SubjectForm()

    return render(request, 'add_subject.html', {'form': form})

@login_required
def student_list(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    students = Korisnik.objects.filter(uloga__naziv='student')
    return render(request, 'student_list.html', {'students': students})


@login_required
def professor_list(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    professors = Korisnik.objects.filter(uloga__naziv='profesor')
    return render(request, 'professor_list.html', {'professors': professors})


@login_required
def add_student(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.uloga = Uloga.objects.get(naziv='student')
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
def add_professor(request):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.uloga = Uloga.objects.get(naziv='profesor')
            professor.password = make_password(form.cleaned_data['password'])
            professor.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'add_professor.html', {'form': form})


@login_required
def edit_student(request, student_id):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    student = get_object_or_404(Korisnik, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

@login_required
def edit_professor(request, professor_id):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')

    professor = get_object_or_404(Korisnik, id=professor_id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'edit_professor.html', {'form': form})


@login_required
def edit_student_upisni_list(request, student_id):
    if request.user.uloga.naziv != 'admin':
        return redirect('home')
    
    student = get_object_or_404(Korisnik, id=student_id, uloga__naziv='student')
    predmeti = Predmet.objects.all().order_by('sem_red')
    upisni_predmeti = UpisniList.objects.filter(student=student)
    semestri = list(range(1, 7))

    if request.method == 'POST':
        if 'predmet' in request.POST:
            predmet_id = request.POST.get('predmet')
            semestar = request.POST.get('semestar')
            predmet = get_object_or_404(Predmet, id=predmet_id)
            UpisniList.objects.create(student=student, predmet=predmet, semestar=semestar)
        elif 'status' in request.POST:
            upisni_list_id = request.POST.get('upisni_list_id')
            status = request.POST.get('status')
            upisni_list = get_object_or_404(UpisniList, id=upisni_list_id)
            upisni_list.status = status
            upisni_list.save()
        return redirect('edit_student_upisni_list', student_id=student_id)

    context = {
        'student': student,
        'predmeti': predmeti,
        'upisni_predmeti': upisni_predmeti,
        'semestri': semestri,
    }
    return render(request, 'student_upisni_list.html', context)

@login_required
def remove_predmet_from_upisni_list(request, student_id, predmet_id):
    student = get_object_or_404(Korisnik, id=student_id, uloga__naziv='student')
    UpisniList.objects.filter(student=student, predmet_id=predmet_id).delete()
    return redirect('edit_student_upisni_list', student_id=student_id)

@login_required
def show_upisni_list(request, predmet_id):
    predmet = get_object_or_404(Predmet, id=predmet_id)
    upisni_list = UpisniList.objects.filter(predmet=predmet)
    return render(request, 'upisni_list.html', {'predmet': predmet, 'upisni_list': upisni_list})


# Student
@login_required
def student_upisni_list(request):
    if request.user.uloga.naziv != 'student':
        return redirect('home')
    
    student = request.user
    upisni_predmeti = UpisniList.objects.filter(student=student)
    predmeti = Predmet.objects.all().order_by('sem_red')
    semestri = list(range(1, 7))

    not_passed_first_year = UpisniList.objects.filter(
        student=student, 
        predmet__sem_red__in=[1, 2]
    ).exclude(status='polozen').exists()
    
    error = ""
    
    if request.method == 'POST':
        if 'predmet' in request.POST:
            predmet_id = request.POST.get('predmet')
            semestar = request.POST.get('semestar')
            predmet = get_object_or_404(Predmet, id=predmet_id)

            if int(semestar) in [5, 6] and not_passed_first_year:
                error = "Niste polozili sve predmete s prve godine"
            else:
                if not UpisniList.objects.filter(student=student, predmet=predmet).exists():
                    UpisniList.objects.create(student=student, predmet=predmet, semestar=semestar)
                upisni_predmeti = UpisniList.objects.filter(student=student)


    context = {
        'student': student,
        'predmeti': predmeti,
        'upisni_predmeti': upisni_predmeti,
        'semestri': semestri,
        'error': error
    }
    return render(request, 'student.html', context)

# Profesor

@login_required
def professor_subjects(request):
    if request.user.uloga.naziv != 'profesor':
        return redirect('home')

    profesor = request.user
    predmeti = Predmet.objects.filter(nositelj=profesor)

    context = {
        'predmeti': predmeti
    }
    return render(request, 'professor_predmeti.html', context)


@login_required
def predmet_details(request, predmet_id):
    if request.user.uloga.naziv != 'profesor':
        return redirect('home')

    predmet = get_object_or_404(Predmet, id=predmet_id)
    
    filter_option = request.POST.get('filter', 'svi')

    if filter_option == 'svi':
        studenti = predmet.upisni_list.all()
    elif filter_option == 'izgubio_potpis':
        studenti = predmet.upisni_list.filter(status='izgubio_potpis')
    elif filter_option == 'dobili_potpis':
        studenti = predmet.upisni_list.filter(status='upisan')
    elif filter_option == 'polozili_predmet':
        studenti = predmet.upisni_list.filter(status='polozen')

    if request.method == 'POST':
        if 'status' in request.POST:
            upisni_list_id = request.POST.get('upisni_list_id')
            status = request.POST.get('status')
            upisni_list = get_object_or_404(UpisniList, id=upisni_list_id)
            upisni_list.status = status
            upisni_list.save()
        elif 'remove' in request.POST:
            upisni_list_id = request.POST.get('upisni_list_id')
            upisni_list = get_object_or_404(UpisniList, id=upisni_list_id)
            if upisni_list.status == 'upisan':
                upisni_list.delete()
    
    context = {
        'predmet': predmet,
        'studenti': studenti,
        'filter': filter_option,
    }
    return render(request, 'predmet_details.html', context)

@login_required
def studenti_10_ects(request):
    students = (
        Korisnik.objects
        .filter(uloga__naziv='student')
        .annotate(total_ects=Sum(F('upisni_list__predmet__ects')))
        .filter(total_ects__gte=10)
    )

    context = {
        'students': students
    }
    
    return render(request, 'studenti_10_ects.html', context)

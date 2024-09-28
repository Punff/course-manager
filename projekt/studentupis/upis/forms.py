# forms.py
from django import forms
from .models import *

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    uloga = forms.ModelChoiceField(queryset=Uloga.objects.all())


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Predmet
        fields = ['naziv', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'nositelj']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['username', 'email', 'password']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['username', 'email', 'password']

# class UpisniListForm(forms.ModelForm):
#     class Meta:
#         model = UpisniList
#         fields = ['predmet', 'semestar']
#         widgets = {
#             'predmet': forms.Select(attrs={'class': 'form-control'}),
#             'semestar': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
# 
# class UpisniListUpdateForm(forms.ModelForm):
#     class Meta:
#         model = UpisniList
#         fields = ['status']
#         widgets = {
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

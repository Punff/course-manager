from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class KorisnikManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
            
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        admin_role = Uloga.objects.get(naziv='admin')
        extra_fields['uloga'] = admin_role
        
        return self.create_user(username, email, password, **extra_fields)


class Uloga(models.Model):
    NAZIV_ULOGA = [
        ('admin', 'Admin'),
        ('profesor', 'Profesor'),
        ('student', 'Student')
    ]
    
    naziv = models.CharField(max_length=50, choices=NAZIV_ULOGA, unique=True)

    def __str__(self):
        return self.naziv


class Korisnik(AbstractUser):
    uloga = models.ForeignKey(Uloga, on_delete=models.CASCADE)

    objects = KorisnikManager()

    class Meta:
        verbose_name = 'korisnik'
        verbose_name_plural = 'korisnici'


class Predmet(models.Model):
    naziv = models.CharField(max_length=100)
    kod = models.CharField(max_length=10)
    program = models.TextField()  
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=3)
    nositelj = models.ForeignKey(Korisnik, limit_choices_to={'uloga__naziv': 'profesor'}, on_delete=models.CASCADE, related_name='predmeti', null=True)

    def __str__(self):
        return self.naziv

class UpisniList(models.Model):
    STATUSI_PREDMETA = [
        ('upisan', 'Upisan'),
        ('polozen', 'Položen'),
        ('izgubio_potpis', 'Izgubio Potpis')
    ]
    
    student = models.ForeignKey(Korisnik, limit_choices_to={'uloga__naziv': 'student'}, on_delete=models.CASCADE, related_name='upisni_list')
    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE, related_name='upisni_list')
    status = models.CharField(max_length=15, choices=STATUSI_PREDMETA, default='upisan')
    semestar = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.predmet} ({self.status})"


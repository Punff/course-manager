from django.contrib import admin
from .models import Korisnik, Uloga, Predmet, UpisniList

admin.site.register(Korisnik)
admin.site.register(Uloga)
admin.site.register(Predmet)
admin.site.register(UpisniList)


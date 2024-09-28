from upis.models import Korisnik

def seed_profesori():
    profesori = [
        {"username": "profesor1", "email": "profesor1@email.com", "password": "pbkdf2_sha256$320000$...", "uloga": 2, "is_staff": True, "is_active": True, "is_superuser": False},
        {"username": "profesor2", "email": "profesor2@email.com", "password": "pbkdf2_sha256$320000$...", "uloga": 2, "is_staff": True, "is_active": True, "is_superuser": False},
        {"username": "profesor3", "email": "profesor3@email.com", "password": "pbkdf2_sha256$320000$...", "uloga": 2, "is_staff": True, "is_active": True, "is_superuser": False},
        {"username": "profesor4", "email": "profesor4@email.com", "password": "pbkdf2_sha256$320000$...", "uloga": 2, "is_staff": True, "is_active": True, "is_superuser": False},
        {"username": "profesor5", "email": "profesor5@email.com", "password": "pbkdf2_sha256$320000$...", "uloga": 2, "is_staff": True, "is_active": True, "is_superuser": False},
    ]

    for data in profesori:
        Korisnik.objects.create(**data)

def seed_predmeti():
    predmeti = [
        {"naziv": "Odabrani alati i naredbe u Linuxu", "opis": "Opis predmeta Odabrani alati i naredbe u Linuxu", "ects_bodovi": 5, "nositelj": 1},
        {"naziv": "Elektroničko poslovanje", "opis": "Opis predmeta Elektroničko poslovanje", "ects_bodovi": 6, "nositelj": 2},
        {"naziv": "Ekonomika i organizacija poduzeća", "opis": "Opis predmeta Ekonomika i organizacija poduzeća", "ects_bodovi": 4, "nositelj": 3},
        {"naziv": "Ronjenje s autonomnom ronilačkom opremom", "opis": "Opis predmeta Ronjenje s autonomnom ronilačkom opremom", "ects_bodovi": 5, "nositelj": 4},
        {"naziv": "Upravljanje poslužiteljima", "opis": "Opis predmeta Upravljanje poslužiteljima", "ects_bodovi": 3, "nositelj": 5},
        {"naziv": "Praktikum iz SQL-a", "opis": "Opis predmeta Praktikum iz SQL-a", "ects_bodovi": 5, "nositelj": 6},
        {"naziv": "Programiranje web korisničkog sučelja", "opis": "Opis predmeta Programiranje web korisničkog sučelja", "ects_bodovi": 7, "nositelj": 7},
        {"naziv": "Projektiranje i upravljanje računalnim mrežama", "opis": "Opis predmeta Projektiranje i upravljanje računalnim mrežama", "ects_bodovi": 6, "nositelj": 1},
        {"naziv": "Analiza 1", "opis": "Opis predmeta Analiza 1", "ects_bodovi": 5, "nositelj": 2},
        {"naziv": "Vođenje projekata i dokumentacija", "opis": "Opis predmeta Vođenje projekata i dokumentacija", "ects_bodovi": 4, "nositelj": 3},
        {"naziv": "Tehnički engleski jezik", "opis": "Opis predmeta Tehnički engleski jezik", "ects_bodovi": 3, "nositelj": 4},
        {"naziv": "Osnove njemačkog jezika", "opis": "Opis predmeta Osnove njemačkog jezika", "ects_bodovi": 6, "nositelj": 5},
        {"naziv": "Uvod u američki film", "opis": "Opis predmeta Uvod u američki film", "ects_bodovi": 4, "nositelj": 6},
        {"naziv": "Izrada web aplikacija", "opis": "Opis predmeta Izrada web aplikacija", "ects_bodovi": 5, "nositelj": 7},
        {"naziv": "Informacijski sustavi", "opis": "Opis predmeta Informacijski sustavi", "ects_bodovi": 6, "nositelj": 1},
        {"naziv": "Programske metode i apstrakcije", "opis": "Opis predmeta Programske metode i apstrakcije", "ects_bodovi": 5, "nositelj": 2},
        {"naziv": "Diskretna matematika", "opis": "Opis predmeta Diskretna matematika", "ects_bodovi": 7, "nositelj": 3},
        {"naziv": "Arhitektura računala", "opis": "Opis predmeta Arhitektura računala", "ects_bodovi": 4, "nositelj": 4},
        {"naziv": "Računalne mreže", "opis": "Opis predmeta Računalne mreže", "ects_bodovi": 5, "nositelj": 5}
    ]

    for data in predmeti:
        Predmet.objects.create(**data)

if __name__ == "__main__":
    seed_profesori()
    seed_predmeti()


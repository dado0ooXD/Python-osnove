# Dictionaries(recnici) su neprimitivni tipovi podataka za skladistenje podataka u 
# key: value (kljuc: vrednost) paru.

# Recnici su kolekcija koja je uredjena(order), promenljiva(changeable),
# i ne dozvoljava duplikate.

# Recnici se zapisuju u viticastim zagradama {}.

automobil = {
    "brend": "passat",
    "boja": "bela",
    "godina": 2012,
    "godina": 2020
}

print(automobil)

# Duzina recnika:
duzina = len(automobil)
print(duzina)

# Ukoliko zelimo da pristupimo nekoj vrednosti iz recnika to mozemo izvrsiti na sledeci nacin.
boja = automobil["boja"]
print(boja)

# 2. nacin 
boja = automobil.get("boja")
print(boja)

# Menjanje vrednosti.
automobil["godina"] = 2014
print(automobil)

# Dodavanje keyeva i vrednosti se moze izvrsiti na 2 nacina:
# 1. nacin:
automobil["hp"] = 140

# 2. nacin je koriscenje update() metode:
automobil.update({"hp": 140})

print(automobil)

# Brisanje odredjenog elementa moze se izvrsiti na 2 nacina:
# 1. nacin:
del automobil["hp"]

# 2. nacin je koriscenje pop() metode:
# automobil.pop("hp")

# Ako zelimo da izbrisemo poslednji element koristi se popitem() metoda:
automobil.popitem()

print(automobil)

# metoda keys nam daje kljuceve za dati recnik.
print(automobil.keys())

# metoda values nam daje vrednosti recnika.
print(automobil.values())

# Recnici mogu sadrzati razlicite tipove podataka.

# metoda items nam vraca listu sacinjenu od tuples(n-torki), gde svaki tuple sadrzi kljuc i vrednost.
print(automobil.items())

# Preko del mozemo izbrisati ceo recnik
# del automobil
# print(automobil)

# clear() metoda ce izbrisati sve elemente recnika:
automobil.clear()
print(automobil)

automobil = {
    "brend": "passat",
    "boja": "bela",
    "godina": 2012,
    "godina": 2020
}

# Ispisivanje vrednosti recnika:
# 1. nacin:
for x in automobil.values():
    print(x)
# 2. nacin:
for x in automobil:
    print(automobil[x])


# Domaci.
# Napraviti recnik student, koji ce sadrzati sledeca svojstva:
# ime, prezime, broj indeksa, godina studija, godina rodjenja, naziv fakulteta.
# Nakon toga izmeniti podatak godina studija,
# izbrisati naziv fakulteta,
# dodati novi element prosecna ocena,
# i na kraju ispisati sve kljuceve i vrednosti jedne ispod drugih, osim godine rodjenja.

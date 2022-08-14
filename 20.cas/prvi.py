# Tuple je kolekcija koja je uredjena(ordered) i nepromenjiva(uncangeable).
# Pise se u obicnim zagradama i dozvoljava duplikate.

# za ispitivanje tuplea koristi se len metoda.

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
print(mytuple)
duzina = len(mytuple)
print(duzina)

# Zapisivanje tuple:
# 1
mytuple = ["skolski pribor", "tabla", "marker", "kreda"]

# 2. 
mytuple =tuple(("skolski pribor", "tabla", "marker", "kreda"))
print(mytuple)

# Ispitivanje tipa:
tip = type(mytuple)
print(tip)

# Tuple moze sadrzati razlicite tipove podataka:
mytuple2 = ("Vahid", 17, False)
print(mytuple2)

# Pristupanje elementima:
broj_godina = mytuple2[1]
print(broj_godina)

# Takodje je dozvoljeno negativno indeksiranje.
mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
print(mytuple[1:])

# Tuple je nepromenljiva kolekcija
# mytuple[2] = "sundjer"  Nije dozvoljeno za tuple
print(mytuple)

# Ako zelimo da izmenimo odredjene elemente u tuple to mozemo odraditi na nacin da prvo
# tuple prevedemo u listu(koja dozvoljava menjanje elementa) i nakon promene vratiti listu u tuple.

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
my_list_tuple = list(mytuple)
print(my_list_tuple)

my_list_tuple[2] = "sundjer"

mytuple = tuple(my_list_tuple)
print(mytuple)

# Kada se radi o dodavanju elemenata u tuple, to  takodje nije dozvoljeno. Medjutim to se moze izvrsiti
# na nacin da se tuple prevede u listu i nakon dodavanja elemenata listi, opet je vratiti u tuple.

# Dodavanje tuplea tupleu.

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
mytuple2 = ["sudjer", "klupa", "stolica"]

mytuple += mytuple2
print(mytuple)

# Kada se radi o brisanju elemenata tuple-a to mozemo izvrsiti preko konvertovanja tuple-a u listu
# i nakon toga izbrisati odredjeni element, te vratiti u tuple

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
my_list_tuple = list(mytuple)
my_list_tuple.remove("tabla")

print(my_list_tuple)
mytuple = tuple(my_list_tuple)

print(mytuple)

# for petlja je dozvoljena kada se radi o tuple:

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
for i in mytuple:
    print(i)

# Dozvoljeno je multiplikatirati tuples.

mytuple = ["skolski pribor", "tabla", "marker", "kreda"]
my_double_tuple = mytuple * 2

print(my_double_tuple)

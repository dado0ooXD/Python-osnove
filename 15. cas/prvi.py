# # Domaci zadatak

# def funkcija():

#     recenica = str(input("- "))

#     print(recenica.upper())
#     print(recenica.lower())
#     print(len(recenica))
#     return(" ")

# print(funkcija())

# Strip() metoda sluzi za brisanje razmaka na krajevima stringa

recenica = "   Danans je suncan dan.     "
print(len(recenica))

skracena_recenica = recenica.strip()
print(skracena_recenica)
print(len(skracena_recenica))

# Replace() metoda - Ona sluzi za menjanje odredjenog slova (niza karaktera), nekim drugim.

recenica = "Raspust traje do 1. septembra."
print(recenica.replace("septembra", "oktobra"))

# Sta ako se data rec ili slovo nadje vise puta u recenici?
nova_recenica = "Raspust traje do 1. septembra ili mozda do 15. septembra."
print(recenica.replace("septembra", "oktobra"))

print(nova_recenica.replace("t", "o"))
# Zakljucak je da replace() metoda menja odredjeni karakter ili niz karaktera onaliko puta koliko se oni nadju u datoj promenljivoj.

# Split() metoda pretvara dati string u listu, ciji su elementi podeljeni na osnovu unetog argumenta metoda.

recenica = "Danas je 15. cas kursa, zamisljeno je da kurs traje 3 meseca , ako se u medjuvremenu nesto ne promeni."
print(recenica.split()) # ako ne stavimo argument unutar split metode, ona ce podeliti string na svaki razmak.

niz1 = recenica.split(", ") #elementi liste su razdvojeni na osnovu ", "
print(niz1[1])

# Escape characters (Izlazni karakteri)

# recenica = "Ti si "kvazi" profesionalac." nije moguce
recenica = "Ti si 'kvazi' profesionalac."
print(recenica)

# 2. nacin
recenica = 'Ti si "kvazi" profesionalac.'
print(recenica)

# \"
recenica = "Ti si \"kvazi\" profesionalac." # 1. primer escape karaktera
print(recenica)
# \'
recenica = 'Ti si \'kvazi\' profesionalac.'  #2. primer escape karaktera
print(recenica)

# n\
recenica = "Danas je 15. cas kursa, \nzamisljeno je da kurs traje 3 meseca , \nako se u medjuvremenu nesto ne promeni."
print(recenica)

# Jos neke metode:
# capitaliza()  metoda pretvara prvi karakter nekog stringa u upper case

recenica = "raspust traje do 1. septembra."
print(recenica.capitalize())

# center(broj) metoda pomera nas string za "broj" mesta. "Iz nekog razloga ta metoda danas nece da radi."
recenica = "raspust traje do 1. septembra."
print(recenica.center(50))

# count("neki karakter(niz karaktera)")  racuna broj ponavljanja nekog karaktera u datom stringu.
recenica = "raspust traje do 1. septembra."
print(recenica.count("a"))

# Domaci:

# 1. Zadatak:
# Prosli domaci zadatak odraditi preko jedne print metode koristeci \n escape karakter.
# 2. Zadatak:
# Napraviti funkciju gde korsinik unosi 2 recenice. Nakon toga ispisati sledece:
# Duzinu prve i druge recenice, duzine prve i druge recenice bez eventualinih razmaka na krajevima recenica,
# prvu recenicu gde zelimo da zamenimo svaki "a" karakter sa "b" karakterom,
# drugu recenicu gde zelimo da zamenimo svaki niz karaktera "raspust" sa nizom karaktera "letnji raspust."
# prvu i drugu recenicu podeljenu na svaki zarez.
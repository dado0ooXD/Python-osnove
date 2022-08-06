#  Stringovi

# Pristupanje odredjenom elementu stringa
a = "Hello World!"
print(a[0])    #Pristupanje prvom karakteru stringa a  
# print(a[len(a)[-1]])    #Pristupanje poslednjem karakteru stringa a (prvi nacin)
print(a[-1])    #Pristupanje poslednjem karakteru stringa a (drugi nacin)

# Listanje elemenata jedan ispod drugog
b = "car"
for i in b:
    print(i)

# Metoda koja vraca duzinu stringa:
b = "Danas je suncan dan."
duzina = len(b)
print(duzina)

# Isapitivanje clanstva:
b = "Danas je suncan dan."
# Proveriti da li se u promenljivoj b nalazi rec "suncan"

if "suncan" in b:
    print("Rec suncan se nalazi u b")
else:
    print("Rec suncan se ne nalazi u b")

# Ispitajte da li se rec "expensive" ne nalazi u sledecoj recenici.
c = "The best things in life are free."

if "expensive" not in c:
    print("Rec se ne nalazi u c")
else:
    print ("Rec se nalazi u c")

# Slicing(secenje) stringa
c = "The best things in life are free."

print(c[4:15])  # best things

print(c[-5:-1])  # 

# Uzimanje dela stringa od odredjenog indeksa pa do kraja.
print(c[4:])

# Uzimanje dela stringa od pocetka do odredjenog indeksa.
print(c[:15])

# Primer
print(c[-14:-10])


# Spajanje stringova:
a = "Danas je"
b = "Suncan dan."
print(a + b)  # 1. nacin
print(a, b)  # 2. nacin
print(f"{a}{b}")  # 3.1. nacin (Format metoda)
print("{}{}".format(a,b))  # 3.2. nacin (Format metoda)

# Pretvaranje celog stringa u velika slova:
c = "The best things in life are free."
print(c.upper())     # Sintaksa je "string" . naziv_metode()


# Pretvaranje celog stringa u mala slova:
c = "The best things in life are free."
print(c.lower())     # Sintaksa je "string" . naziv_metode()

# Domaci zadatak.
# Napraviti funkciju koja od korisnika trazi unos recenice.
# Funkcija treba da vrati recenicu u sledecim oblicima:
# Recenicu ispisana velikim slovima,
# Recenicu ispisana malim slovima,
# Duzinu unete recenice. 
# Danas radimo funkcije

# Funkcija predstavlja blok koda koji ce se izvrsiti samo u slucaju pozivanja.

# sintaksa:
from re import A
from tkinter import Y


def naziv_funkcije():
    # kod za izvrsavanje
    print("Odstampaj nesto.")

naziv_funkcije()

# 1. varijanta je uesto print(...) koristimo rec return

def druga_funkcija():
    # kod za izvrsavanje
    a = 5
    return a

print(druga_funkcija())

# Napraviti funkciju sa nazivom pozdrav, koja vraca recenicu "Zdravo svima." na dva nacina.
# Preko print i preko return.

def pozdrav():
    print("Zdravo svima.")

pozdrav()


def pozdrav2():
    recenica = "Zdravo svima."
    return recenica
# moze i "Zdravo svima."
# Nakon return unutar funkcije nijedna naredba se nee izvrsiti!
# return staviti iskljucivo na kraju!
print(pozdrav2())

# Svaka funkcija moze sadrzati parametre ili (argumente) u sebikoje ce koristiti za izvrsavanje odredjenog posla.

def vraca_zbir(a,b): # a i b predstavljaju parametre unutar funkcije
    return a+b

print(vraca_zbir(4,10)) # 4 i 10 predsavljaju argumente.

# Pozivanjem funkcije moramo staviti onaliko argumenata koliko smo definisali parametara prilikomm definisanja funkcije.

def proizvod(x,y): # moguce su defaultne vrednosti, ali njih je potrebno definisati kao poslednje.
    return x*y

print(proizvod(4,5))

# Napraviti funkciju koja vraca kolicnik dva broja. U slucaju da je delilac jednak nuli imamo poruku deljenje nije moguce izvrsiti. 
# Takodje neka delilac ima defaultnu vrednost 1.

def kolicnik(x,y=1):
    if y==0:
        return "Deljenje nije moguce"
    return x/y

print(kolicnik(10,2))
print(kolicnik(10,0))
print(kolicnik(10))
print(kolicnik()) # Greska jer funkcija ocekuje bar jednu vrednost: a b je definisan

prom1 = 17
def vrati_prom():
    prom1 = 14
    print(prom1)

vrati_prom()

print(prom1)

# Promenjljiva definisana unutar prostora funkcije je vidljiva samo unutar te funkcije. Ako je pozovemo van nje, program je nece prepoznati.

def vrati_nesto():
    prom2 = 16
    print(prom2)

# print(prom2) ne izbacuje nista.

# Zadaci:
# 1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata. Odnosno povrsinu kvadrata ako su dva
# data argumenta jednaka.

# 2. Napraviti funkciju koja pretvara broj ince u centimetre.
# Pozivanjem funkcije treba uneti broj inca.
# Zadaci:
# 1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata. Odnosno povrsinu kvadrata ako su dva
# data argumenta jednaka.

# 2. Napraviti funkciju koja pretvara broj ince u centimetre.
# Pozivanjem funkcije treba uneti broj inca.

# 1.

from re import A


def funkcija(a,b=9):
    if a==b:
        return a*a
    return a*b

print(funkcija(4,4))


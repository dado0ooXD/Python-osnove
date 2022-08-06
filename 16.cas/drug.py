# Radno vreme jedne organizacije he izmedju 9 i 17.Odrediti da li je poslati mail stigao u toku radnog vremena
# 9h spada u radno vreme(stampa Da), dok 17 ne spada(stampa Ne)


def funkcija():

    sat = (int(input("Unesite sat: ")))
    minut = (int(input("Unesite minut: ")))
    if sat in range(9,17):
        print("Da")
    else:
        print("Ne")

funkcija()

# Domaci.
# Koristeci bool () funkciju ispitati sledece stvari:
lista1 = [0]
# 1. Da li je string koji je uneo korisnik True ili False.
# 2. Da li je broj koji je uneo korisnik True ili False.
# 3. Da li je lista1 True ili False.
# 4. Uporediti dva uneta broja od strane korisnika.
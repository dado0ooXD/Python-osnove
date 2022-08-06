# Domaci.
# Koristeci bool () funkciju ispitati sledece stvari:
lista1 = [0]
# 1. Da li je string koji je uneo korisnik True ili False.
# 2. Da li je broj koji je uneo korisnik True ili False.
# 3. Da li je lista1 True ili False.
# 4. Uporediti dva uneta broja od strane korisnika.

string = str(input("Unos stringa: "))
print(bool(string)) 

broj = int(input("Unos broja: "))
print(bool(broj))

print(bool(lista1))

prvibroj = int(input("Prvi: "))
drugibroj = int(input("Drugi: "))

if bool(prvibroj>drugibroj):
    print("Prvi broj je veci od drugog")
elif bool(prvibroj<drugibroj):
    print("Prvi broj je manji od drugog broja")
else:
    print("Prvi uneti broj je jednak drugom")


# 5. Primer
for i in range (10,0,-1):  # Ako se radi o opadajuce nizu, neophodno je definisati treci argument(-1).
    print(i)

# 6. Primer (iteracija kroz listu)
lista1 = ["tastatura","mis", "maticna ploca", "graficka kartica", "procesor"]
for komp in lista1:
    print(komp)

# 7. Primer (Nested for loop - Ugnjezdene for petlje)
lista1 = [1,2,3,4,5]
lista2 = ["tastatura","mis", "maticna ploca", "graficka kartica", "procesor"]
for i in lista1:
    for j in lista2:
        print(i,j)

# 8. Primer 
# Sintaksa za pristup odredjenom elementu iterirajuce promenljive:
recenica = "Danas je suncan dan."
# Pronaci prvi karakter nase recenice:
prvi = recenica[0]
print(prvi)
print(recenica[6])
# Izvuci iz lista2 maticnu plocu:
print(lista2[2])

# Pomocu ugradjene funkcije len() mozemo dobiti duzinu liste.
duzina = len(lista2)
print(duzina)

duzina_rec = len(recenica)
print(duzina_rec)

# 8. Primer
for i in range(0,len(lista2)):
    # print(i) ovako dobijamo indekse nase liste
    # print(lista2[i]) ovako dobijamo elemente nase liste.
    print(i, lista2[i])  #izvrsili smo print indeksa i elementa na tom indeksu

# 9. Primer 
for i in recenica:  
    print(i) # izbacuje recenicu tako da slova budu jedna ispod drugih.

# 10. Primer 
for i in range(0,len(recenica)):
    print(i, recenica[1])


# Dve nove naredbe:
# 1. break - Predstavlja prekid iteracije ako je odredjeni uslov zadovoljen.
# 2. continue - Predstavlja da se "zaobidje" odredjeni element ako je pod uslovom.

# 11. Primer
for i in lista2:
    if i == "mis":
        break
    print(i)

# 12. Primer
for i in lista2:
    if i =="mis":
        continue
    print(i)

# Domaci zadatak:
# 1. Zadatak:
# Napraviti dva niza od po 6 elemenata. Neka se izvrsi tako da se element prvog niza prikaze onaliko puta koliko ima elemenata drugog niza
# a pritom i svaki element drugog niza (ugnjezdena for petlja)

# 2. Zadatak:
# Ispitati sve parne prirodne brojeve od 10 do 110 (ukljucujuci oba) izuzev 16, 22, 44, 66, 88, 102, 108.

# 3. Zadatak:
# ispisati sve elemente prethodno definisane liste od 10 elemenata odpozadi. 5 primer

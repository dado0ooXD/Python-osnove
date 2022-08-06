# Domaci zadatak:
lista1 = ['Mercedes', 'Audi', 'Fiat', 'Porsche', 'Passat']
lista2 = [2008, 2014, 2002, 2019, 2005]
# Uporediti duzine prve i druge liste, if naredba
# Dodati u prvoj listi na pocetnom indeksu "BMW",
# Zatim dodati godinu tog automobila na istoj poziciji, ali u drugoj listi,
# Izmeniti poslednja 2 elementa sa neka druga 2(za prvu i za drugu listu)
# Nakon svega dodati u obe liste kao poslednji element neku listu sa po 3 elementa
# razlicitih tipova poadataka.

# if lista1 > lista2:
    # print("Prva lista je duza od druge.")
# elif lista1 < lista2:
#     print("Druga lista je duza od prve.")
# else:
#     ("Ove dve liste su jednake.")

lista1.insert(0, "BMW")
print(lista1)

lista2.insert(0, 1945)
print(lista2)

lista1[3: ] = "Ferari", "Ford"
print(lista1)

lista2[3: ] = 2012, 2015
print(lista2)

intlist = [1, 2, 3]
strlist = ["Buggati", "Citroen", "Jeep"]
dictlist = {"Ime i godine" : "Davud" "17" }

lista1.append(intlist)
lista1.append(strlist)
lista1.append(dictlist)

print(lista1)

lista2.append(intlist)
lista2.append(strlist)
lista2.append(dictlist)

print(lista2)

# Liste
# Elementi unutar liste su:
# poredjani, 
# promenljivi,
# dozvoljavaju duplikate.

# U drugim programskim jezicima liste se nazivaju nizovima (Array).

# Liste u Pythonu mogu sadrzati razlicite tipove podataka:
lista1 = ["Ensar", "Hana", "Vahid", 17, 16, 17]
print(lista1)

duzina = (len(lista1))
print(duzina)

lista2 = ["Aldin", "Davud", 17, 17, True, False, [1,2,3], ("abc")]
print(lista2)

# Pristupanje elementima:

print(f"{lista1[1]} ima {lista1[-1]} godina ")
print(f"Tvrdnja da {lista2[1]} ima {lista2[3]} godina je {lista2[4]}")

# Menjanje vrednosi nekog elementa liste:

voce = ["breskva", "bostan", "kajsija", "dinja", "banana"]
print(voce)

voce[2] = "kivi"
print(voce)

voce[2: ] = ["ananas", "jagoda", "jabuka"]
print(voce)

voce[2: ] = ["kruska", "sljiva", "narandza", "grejpfrut", "mango", "smokva"]
print(voce)

# Liste su promenljive. Mozemo izmeniti odredjeni element liste pristupanjem njemu preko indeksa.
# Svakako mozemo izmeniti vise elemenata odjednom.
# Takodje nam je dozvoljeno da ovakvim izmenama prosirimo nasu listu.
# Sve spomenuto je odradjeno u primerima iznad.

# insert() metoda nam sluzi za dodavanje elementa listi na tacno odredjenom indeksu.
voce = ['breskva', 'bostan', 'kruska', 'sljiva', 'narandza', 'grejpfrut', 'mango', 'smokva']
voce.insert(1, "nar")
print(voce)

voce.insert(3, ["tresnja", "nektarina"])
print(voce)

# append() metoda nam sluzi za dodavanje elementa na kraju liste.
voce.append("jabuka")
print(voce)


# Domaci zadatak:
lista1 = ["Mercedes", "Audi", "Fiat", "Porsche", "Passat"]
lista2 = [2008, 2014, 2002, 2019, 2005]
# Uporediti duzine prve i druge liste, if naredba
# Dodati u prvoj listi na pocetnom indeksu "BMW",
# Zatim dodati godinu tog automobila na istoj poziciji, ali u drugoj listi,
# Izmeniti poslednja 2 elementa sa neka druga 2(za prvu i za drugu listu)
# Nakon svega dodati u obe liste kao poslednji element neku listu sa po 3 elementa
# razlicitih tipova poadataka.
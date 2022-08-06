lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]
# kroz iteraciju date liste ispisati "BANANA" za svaki element osim gde se nadje "dinja".

lista2 = [i if i == "dinja" else "BANANA" for i in lista]
print(lista2)

# Sortiranje liste. sort() metoda
# 1. Sortiranje prema slovima:

lista = ["kajsija", "ananas", "kruska", "banana", "dinja", "jabuka"]
lista.sort()
print(lista)

# Obrnnuti alphabet
lista.sort(reverse=True)
print(lista)

# 2. Sortiranje prema brojevima:
lista2 = [34, 44, 2, 7, 1, 58, 98]
lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

# Po defaultu sort() metoda je (case sensitive)
# Prednost imaju velika slova u odnosu na mala
lista = ["Kajsija", "ananas", "Kruska", "Banana", "dinja", "jabuka"]
lista.sort()
print(lista)

# U slucaju da zelimo ukinuti prednost velikih slova u odnosu na mala, to mozemo uciniti a sledeci nacin:
lista = ["Kajsija", "ananas", "Kruska", "Banana", "dinja", "jabuka"]
lista.sort(key=str.lower)
print(lista)

# reverse () metoda sluzi za vracanje liste obrutim redosledom u zavisnosti od redosleda pisanja elementa u llsti.
lista = ["kajsija", "ananas", "kruska", "banana", "dinja", "jabuka"]
lista.reverse()
print(lista)

lista2 = [34, 44, 2, 7, 1, 58, 98]
lista2.reverse()
print(lista2)

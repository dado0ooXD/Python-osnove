# extend() omogucava spajanje 2 liste 

voce = ["jabuka", "tresnja", "banana"]
tropsko = ["mango", "ananas"]

voce.extend(tropsko)

# extend() metoda pored liste mozedodati tuple, set, dictionary...


# pop () metoda sluzi za brisanje elemenata liste.
# Mozemo izbrisati specificni element (dodavanjem indeksa kao arg metode), 
# ili poslednji element liste (izostavljajuci argument metode).

voce.pop(2)
print(voce)

voce.pop()

izbrisana_stavka = voce.pop()   # mozemo sacuvati kao promenljivu izbrisanu stavku iz liste
print(voce)

print(izbrisana_stavka)  

# del keyword
# del mozemo koristiti za brisanje odredjenog elementa lista kao i brisanje kompletne liste


# Brisanje elementa liste.
del voce[0]
print(voce)

# Brisanje cele liste.
del voce 
# print(voce)

# clear () metoda sluzi za brisanje svih elemenata liste
voce = ["jabuka", "tresnja", "banana"]
print(voce)
voce.clear()
print(voce)

# Ispisati elemente liste jedan ispod drugog, gde je drugo slovo elementa a.
lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]

for i in lista:
    if i[1]=="a":
        print(i)

# Saciniti lista2 da bude od istih elemenata kao i lista1.
lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []

for i in lista1:
    lista2.append(i)

print(lista2)

# 2. nacin 

lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []

lista2 = [i for i in lista1]
print(lista2)

# Jos jedan primer
lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []

lista2 = [i for i in lista1 if i[-1] == "a"]
print(lista2)

# Napraviti listu od elemenata od 1-10 na nacin kakav smo radili u prethodnom primeru.
lista3 = [i for i in range(1,11)]
print(lista3)

lista4 = [i for i in range (1,11) if i%2==0]
print(lista4)

# Napraviti novu listu sacinjen od elemenata lista5 samo u slucaju da naidjemo na bananu ispisati narandzu.
lista5 = ["ananas", "banana", "kruska", "dinja"]

lista6 = [i if i!= "banana" else "narandza" for i in lista5]
print(lista6)

# Zakljucak.
# Ako imamo jedan uslov onda cemo ispisati na sledeci nacin:
# lista2 = [i for i in lista1 if i[-1] == "a"]
# Ako imamo vise uslova onda cemo ispisati na ovaj nacin:
# lista6 = [i if i!= "banana" else "narandza" for i in lista5]

# Domaci.
# Napraviti 2 liste po svojoj zelji, neka imaju po 5 elemenata.
# dodati drugu listu prvoj,'
# izbrisati prvi i poslednji element prosirene liste,
# napraviti novu listu koja ce biti sadrzana od onih elemenata poslednje uredjene liste,
# za koje vazi da je prvi karakter jednak stringu "a",
# napraviti jos jednu listu koju cine elementi poslednje izmenjene liste, ali da svi budu ispisani
# velikim slovima.





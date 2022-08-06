# Domaci.
# Napraviti 2 liste po svojoj zelji, neka imaju po 5 elemenata.
# dodati drugu listu prvoj,'
# izbrisati prvi i poslednji element prosirene liste,
# napraviti novu listu koja ce biti sadrzana od onih elemenata poslednje uredjene liste,
# za koje vazi da je prvi karakter jednak stringu "a",
# napraviti jos jednu listu koju cine elementi poslednje izmenjene liste, ali da svi budu ispisani
# velikim slovima.

from re import I


lista1 = ["a", "b", "c", "d", "e"]
lista2 = ["1", "2", "3", "4", "5"]

lista1.extend(lista2)
print(lista1)

lista1.pop(0)
lista1.pop(-1)
print(lista1)

lista3 = [i for i in lista1 if i[0] == "a"]
print(lista3)







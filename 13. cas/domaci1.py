# 1.
lista1 = [1,5,4, "Market", "Ulica", "Park"]
def vrednosti_indeksa(lista):
    duzina = len(lista)
    for i in range (0,duzina):
        print(i, lista[i])

vrednosti_indeksa(lista1)


# 2. 
lista3 = [1,2,3,4,5]
def zbir_elemenata(lista):
    zbir_elemenata = 0
    for i in lista:
        zbir_elemenata += i
    return zbir_elemenata

print(zbir_elemenata(lista3))

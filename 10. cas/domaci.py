# 2. Zadatak 
for i in range (10,111,2):
    if i == 16 or i == 22 or i == 44 or i == 66 or i == 88 or i == 102 or i == 108:
        continue
    print(i)


# 3. Zadatak

lista = ["jabuka", "kruska", "jagoda", "tresnja", "malina", "breskva", "kivi", "banana", "mango","ananas"]

duzina = len(lista)
print(duzina)
for i in range(duzina -1,-1,-1):
    print(lista[i])
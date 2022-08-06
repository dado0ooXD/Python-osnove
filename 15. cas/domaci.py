# 2.
def funkcija():

    prva_recenica = str(input("prva:"))
    druga_recenica = str(input("druga:"))

    print(len(prva_recenica))
    print(len(druga_recenica))

    print(prva_recenica.replace("a", "b"))
    print(druga_recenica.replace("raspust", "letnji raspust"))

    print(prva_recenica.split(" "))
    print(druga_recenica.split(" "))

print(funkcija())


# 1.
def funkcija ():
    recenica = str(input("- "))
    print(f"{recenica.upper()}\n{recenica.lower()}\n{len(recenica)}")

funkcija()

# 2.

def funkcija2():
    recenica1 = str(input("Unesite prvu recenicu: "))
    recenica2 = str(input("Unesite drugu recenicu: "))
    print(f"Duzina prve recenice je {len(recenica1)}")
    print(f"Duzina druge recenice je {len(recenica2)}")
    print(f"Duzina prve recenice koriscenjem strip()metode iznosi: {len(recenica1.strip())}")
    print(f"Duzina druge recenice koriscenjem strip()metode iznosi: {len(recenica2.strip())}")
    print(recenica1.replace("a", "b"))
    print(recenica2.replace("raspust", "letnji raaaspust"))
    print(recenica1.split(", "))
    print(recenica2.split(", "))

funkcija2()
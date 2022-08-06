#  1. 

a = int(input("Unesite prvi pozitivan broj:"))
b = int(input("Unesite drugi pozitivan broj:"))

if a==b:
    print(f"Povrsina kvadrata je {a*b}")
else:
    print(f"Povrsina pravouganika je {a*b}")


# 2.

x = int(input("Unesite neki ceo broj: "))

if x>10 and x<=50:
    print("Pripada.")
else:
    print("Ne pripada.")

# 2 nacin

if x in range(11,51):
    print("Pripada")
else:
    print("Ne pripada.")



# 3

x = float(input("Unesite prvi realan broj: "))
y = float(input("Unesite drugi realan broj: "))

if y==0:
    print("Deljenje je nemoguce.")
else:
    print(f"Kolicnik dva uneta realna broja je {x/y}")
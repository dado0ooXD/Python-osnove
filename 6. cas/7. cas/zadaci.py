# 1. Napisati program koji proverava da li je uneti ceo broj x paran ili neparan ili
# i ispisuje odgovarajucu poruku.

x = int(input("Unesite broj: "))

if x%2==0:
    print("Uneti broj je paran. ")
else:
    print("Uneti broj je neparan. ")


# Napisati program koji, ako je uneti broj veci od 0, stampa poruku broj je pozitivan.
# Obuhvatiti i slucajeve kad je broj manji od nule i jednak nuli.

x = int(input("Unesite broj: "))

if x>0:
    print("Uneti broj je pozitivan.")
elif x<0:
    print("Uneti broj je negativan.")
else: 
    print("Uneti broj je jednak nuli.")

# 3. Napisati program koji, proverava da li je zbir 2 uneta broja deljiv sa 3 ili nije. 
# Ispisati poruku jeste ili nije.


x = int(input("Prvi broj."))
y = int(input("Drugi broj."))

if (x+y)%3==0:
    print("Deljiv je.")
else:
    print("Nije deljiv.")

# Domaci zadaci:
# 1. zadatak Napisati program koji se unose 2 pozitivna cela broja a i b. Napisati program koji
# izracunava i stampa povrsinu kvadrata ako su uneti brojevi jednaki,
#  odnosno povrsinu pravougaonika ako su brojevi razliciti.
# Uneti brojevi predstavljaju stranice pravougaonika odnosno kvadrata.

# 2. Proveriti da li uneti broj x pripada intervalu (10, 50}.  10 se ne ukljucuje    x>10  x<=50
# ispisati poruku "Pripada" ili "Ne pripada".

# 3 Korisnik unosi 2 realna broja x i y. Napisati program koji izracunava i stampa, kolicnik (x:y) ako je
# broj y razlicit od nule, a inace ispisuje poruku deljenje je nemoguce.
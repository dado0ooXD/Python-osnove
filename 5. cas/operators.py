# Operatori
# Operatori se koriste za izvrsavanje brojnih racunskih operacija promenljivih.

# Navest cemo 6 vrsta operatora.
# 1. Aritmeticki operatori.  Koriste se za izvrsavanje raznih operacija medju promenljivim.
#   1. +  Sabiranje            => x+y
#   2. - Oduzimanje            => x-y
#   3. * Mnozenje              => x*y
#   4. / Deljenje              => x/y
#   5. % Moduo                 => x%y (5%3=2) 
#   6. ** Stepenovanje         => x**y (2**3=8)
#   7. // Deljenje bez ostatka => x//y (10//3=3)

# 2 Operatori dodele vrednosti (Assignent operators)

#    1. =    =>  x=5
#    2. +=   =>  x+=3 (x=x+3)

x= 10
print(x)
x+=3
# x je imalo vrednost 10. Nakon toga smo dodali 3. (x+=3) i sada x iznosi 13
print(x)

#  3. -=   => x-=3 (x=x-3)
#  4. *=   => x*=3 (x=x*3)
#  5. /=   => x/=3 (x=x/3)
# 6. % = => x%=3 (x=x%3)

x=11
print(x)
x%=3 
print(x)

#  7. **=  => x**=3 (x=x**3)

x=5
print (x)
x**=3 
print(x)

#  8. Deljenje bez ostatka //=  => x//=3 (x=x//3)

x=12
print(x)
x//=5
print(x)

#     3 Operatori poredjenja. Koriste se za poredjenje dve vrednosti.

#  1. ==    Jednakost  =>   x==y

print(5==5)
print(4==9)

# 2. !=     Nejednakost =>  x!=y

print(4!=6) 
# != ispitujemo da li je 4 razlicito od 6 = true
print(8!=8)

# 3. > Vece od  =>  x>y

print(3>8)

# 4. < Manje od  => x<y
print(3<8)

# 5.  >= Vece ili jednako  => x>=y

print(5>=5)

#  >= Manje ili jednako x<=y
print(4<=5)

#     4. Logicki operatori. Koriste se u kombinovanju kondicionala.

# 1. and  x<5 and x<10 moraju biti zadovoljeni i jedan i drugi 
# 2. or x<5 or x<4
# 3. not (okrece rezultat) 

x=5
y=3
print(x==y)
print(not(x==y))

#  Domaci. Odraditi po jedan primer za svaki predjeni operator danas. 7 Aritmetickih, 8 operatora dodele vrednosti,
#  6 operatora poredjenja i 3 logicka operatora.

#     5. Identicki operatori 

# Koriste se za uporedjivanje objekata. 
# Ne ako su jednako vec ako su zapravo isti objekat, sa isto memorijskom lokacijom.
# 1. is =>   x is y
# 2. is not =>   x is not y



x = 5
y = 5
print(x is y)

niz1 = [1,2,3,4]
niz2 = niz1

print(niz1 is niz2)
print(niz1 is not niz2)

x="Neki string"
y="Neki string"
print(x is y)

#     6. Operatori clanstva
#  Koriste sa za ispitivanje da li je odredjeni niz prisutan u nekom objektu.

# 1. in      =>  x in y 
# 2. not in  =>  x not in y

list1= ["banana", "jabuka", "ananas", "jagoda"]
banana = "banana"

print("banan" in list1)

print("dinja" not in list1)




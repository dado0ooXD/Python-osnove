# Python Copy lists
voce = ["jagoda", "ananas", "nar", "smokva"]
# povrce = ["krompir", "luk", "sargarepa"]

# copy() metoda sluzi za pravljenje nove liste sacinjene od elemenata stare liste

voce2 = voce.copy()
print(voce2)

# Mozemo jednostavno reci da je neka promenljiva, npr voce3 = voce
# Medjutim to nije dobra praksa iz razloga sto bilo kakva promena unutar bilo koje od te dve liste
# ce se odraziti na onu drugu.
# Zapravo, na taj nacin smo novu listu identicki izjednacili sa starom listom

voce3 = voce
print(voce)

voce[2] = "grozdje"
print(voce3)
print(voce)

# Jos jedan nacin kopranja liste je:
voce = ["jagoda", "ananas", "nar", "smokva"]
voce4 = list(voce)
print(voce4)

voce4[0] = "tresnja"
print(voce4)
print(voce)

# Pridruzivanje liste.
# Koristili smo extend() metodu.
# Jos jedan nacin je:

voce = ["jagoda", "ananas", "nar", "smokva"]
povrce = ["krompir", "luk", "sargarepa"]

voce_i_povrce = voce + povrce
print(voce_i_povrce)



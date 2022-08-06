broj_godina = int(input("Unesite svoj broj godina: "))
visina = int(input("Unesite svoju visinu: "))
tezina = int(input("Unesite svoju tezinu: "))

print(broj_godina, visina, tezina)

prvi_iznos = 2
drugi_iznos = 4
treci_iznos = 5

prva_recenica = f"Danas sam dobio {prvi_iznos} ocene, iz biologije {drugi_iznos}, a iz geografije {treci_iznos}.".format(prvi_iznos, drugi_iznos, treci_iznos)
print(prva_recenica)
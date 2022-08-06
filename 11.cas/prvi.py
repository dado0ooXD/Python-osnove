# Zadaci
Hana_m = int(input("Broj bodova iz matematike: "))
Hana_p = int(input("Broj bodova iz programiranja: "))

Seid_m = int(input("Bodovi iz matematike: "))
Seid_p = int(input("Bodovi iz programiranja: "))




if Hana_m + Hana_p > Seid_m + Seid_p:
    print(1)

elif Hana_m + Hana_p < Seid_m + Seid_p:
    print(2)

elif Hana_m + Hana_p == Seid_m + Seid_p:
    if Hana_m + Hana_p > Seid_m + Seid_p:
        print(1)
    elif Hana_m + Hana_p < Seid_m + Seid_p:
        print(2)
    else:
            print(1)
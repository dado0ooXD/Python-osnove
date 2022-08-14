import datetime

trenutno_vreme = datetime.datetime.now()
print(trenutno_vreme)

datum_rodjenja = datetime.datetime(2004, 9, 30, 9, 00, 00)
print(datum_rodjenja)

dan_rodjenja = datum_rodjenja.strftime("%a")
print(datum_rodjenja)

mesec_rodjenja = datum_rodjenja.strftime("%B")
print(mesec_rodjenja)

datum2 = datetime.datetime(2004,9,30)
print(datum2)
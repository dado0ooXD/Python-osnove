# Domaci.
# Napraviti recnik student, koji ce sadrzati sledeca svojstva:
# ime, prezime, broj indeksa, godina studija, godina rodjenja, naziv fakulteta.
# Nakon toga izmeniti podatak godina studija,
# izbrisati naziv fakulteta,
# dodati novi element prosecna ocena,
# i na kraju ispisati sve kljuceve i vrednosti jedne ispod drugih, osim godine rodjenja.

student = {
    "ime": "Davud",
    "prezime": "Carovac",
    "broj_indeksa": 2594,
    "godina_sudija": "cetvrta",
    "godinarodjenja": 2004,
    "nazivfakulteta": "Metropolitan Beograd"
}

student["godina_studija"] = "druga"
student.pop("nazivfakulteta")
student["prosecna_ocena"] = 8

print(student)

for i,x in student.items():
    if i == "godinarodjenja":
        continue
    print(i,x)




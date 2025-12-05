# kérjen be egy szöveget, és egy betűt
#adja meg, hogy hány darab betű van a szövegben
betuk=0
szerepel=0
szoveg=input("Adjon meg egy szöveget ")
betu=input("Adjon meg egy betűt.")
index=0
while (index>len(szoveg) and szoveg[index] != betu):
    index+=1
for karakter in szoveg:
    betuk+=1
    if karakter == betu:
        szerepel+=1

print(f"{betuk} darab betű van a szövegben, a megadott betű {szerepel} alkalommal szerepel a szövegben")


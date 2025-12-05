#Egy szövegben hány darab szóköz van?

szoveg=input("Adjon meg egy szöveget: ")
db=0

for karakter in szoveg:
    if(karakter==" "):
        db+=1

print(db, "Darab szóköz van")

#adja meg, hogy a szövegben van-e cs betű (két karakter egymás mellett)
#pl.: alma, kacsa, filc
csdarab=0
folosleg=0
for karakter in range(len(szoveg)-1):
    if(szoveg[karakter]=="c"):
        if szoveg[karakter+1]=="s":
            csdarab+=1

print(csdarab, "Darab cs betű van benne.")
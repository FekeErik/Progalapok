"""
Elől tesztelős ciklus
while ciklus

-Nem tudjuk, hányszor fog ismétlődni.
Feltételhez kötött 
-Akkor ismétel, ha feltétel igaz

while(feltétel):
    utasítások
"""

#generáljon véletlen számot 0-és 10 között, amíg nullát nem kapunk
import random

szam=random.randint(0,10)
print(szam)
while szam !=0:
    szam=random.randint(0,10)
    print(szam,end=" ")

#kérjen be számokat, amíg felhasználó nem ad meg nullát.

ad=int(input("Adjon meg egy számot."))
osszeg=0
db=0

while ad!=0:
    osszeg+=ad
    db+=1
    ad=int(input("Adjon meg NULLÁT."))
    
print("Nagyon profi vagy")
print(round(osszeg/db,2))

# Adott egy szöveg
Bekeres=input("Adjon meg egy szöveget")
#Adja meg hogy van e benne x betű
if("x" in Bekeres):
    print("Van benne X!!!")
else:
    print("Nincs benne X.")
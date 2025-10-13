import random

#generaljon harom veletlen haromjegyű számot, melyek 13-mal oszthatóak.
#állítsa ezeket sorrendbe
#adja meg az átlaguk
#van-e közöttük 4-el végződő?

szamok=[]
oszthato=0
nemoszthato=0
szam=random.randint(100,999)

print(szamok)

if(szam % 13 == 0):
    oszthato+=1
else:
    nemoszthato+=1

print("Mittudomen")

if oszthato>=1:
    print("Van osztható")
else:
    print("nincs osztható szám, git gud")
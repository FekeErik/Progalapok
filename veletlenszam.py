import random

#generálj ki 10 darab véletlen számot
#írassa ki a számok összegét

osszeg=0
for a in range(0,11,1):
    velSzam=random.randint(1,9)
    osszeg+= velSzam
    print(velSzam, end=" ")
print()
print("Összeg",osszeg)

#hány darab páros véletlen számot generált ki?
#melyik a legnagyobb véletlen szám?
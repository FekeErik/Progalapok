import random
import math

#1 feladat
szerencse=random.randint(0,9)
if szerencse == 1 or szerencse==6:
    print("labda")
elif(szerencse == 2 or szerencse==7):
    print("ceruza")
elif(szerencse== 3 or szerencse==8 ):
    print("Színes papír")
elif(szerencse==4 or szerencse==9):
    print("Bicikli")
else:
    print("nem nyert")

#2. feladat
ora=int(input("adja meg az eltöltött időt, órában."))
het=ora//168
nap=(ora - het * 168)//24
ora2= (ora - het * 168)//24 - nap * 24 #ora % 24
print("Átszámolva:", het, "hét", nap, "nap", ora2, "ora")

#3. feladat
szam=random.randint(100,999)
print("A generált háromjegyű szám:",szam)
elso=szam//100
masodik=szam - (elso * 100) //10

#4. feladat

a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
print("Véletlen számok:",a,b,c)

if(a!=0 and b!=0 and c!=0):
    harmonik = 3 / (1/a + 1/b + 1/c)
elif(a==0 and b!=0 and c!=0):
    harmonik=2/(1/c)
elif(b==0 and a!=0 and c!=0):
        harmonik = 2/(1/b)
elif(c==0 and b!=0 and a!=0):
    harmonik = 2/(1/a)
else:
    print("nincs megoldás")
print("Harmonikus közép", round(harmonik,3))
import random
import math

n = 30
lista = []

for i in range(0,n,1):
    valtozo=random.randint(10,99)
    veletlen=random.randint(1,2)
    if(veletlen==1):
        lista.append(valtozo*100+17)
    else:
        lista.append(valtozo*100+13)

print(lista)

osszeg=0
for elem in lista:
    osszeg+=elem
#atlag = osszeg/len(lista)
atlag=osszeg/n
print(round(atlag,2))

dba = 0
for index in range(0,n,1):
    #if(atlag>lista[index]):
    if lista[index]<atlag:
        dba+=1
print("számtani átlag alatti értékek száma:",dba)


szorzat = 1
for elem in lista:
    szorzat *= elem
matlag=math.pow(szorzat,1/n)

#mértani átlag alatti számok összege
mossz=0
for a in lista:
    if(matlag>a):
        mossz+=a
print("Mértani átlag alatti számok összege: ",mossz)


szoveg=input("Adjon meg egy szöveget: ")
print(szoveg)
betu = input("Adjon meg egy betűt: ")

dbv=0
for karakter in szoveg:
    if karakter==betu:
        dbv+=1
print(dbv)

szo1=input("Adjon meg egy szöveget: ")
szo2=input("Adjon meg egy szöveget: ")

minimumhossz=0
kulonbseg=0

if(len(szo1)>len(szo2)):
    minimumhossz=len(szo2)
else:
    minimumhossz=len(szo1)
for i in range(0,minimumhossz,1):
    if (szo1[i] !=szo2[i]):
        kulonbseg+=1
print(kulonbseg)
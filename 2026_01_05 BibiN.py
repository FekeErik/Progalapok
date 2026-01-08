#generáljon egy listában olyan négyjegyű számokat, melyek 3,5, vagy 7-re végződnek
#hány darab ilyen szám van?

import random
lista=[]

for i in range(13):
    valtozo = random.randint(1000,9999)
    veletlen = random.randint(1,3)
    if veletlen == 1:
        lista.append(valtozo*10+3)
    elif veletlen == 2:
        lista.append(valtozo*10+5)
    else:
        lista.append(valtozo*10+7)
print(lista)

haromra=0
otre=0
hetre=0

for i in range(len(lista)):
    if lista[i] % 10 == 3:
        haromra+=1
print(haromra)

for i in range(len(lista)):
    if lista[i] % 10 == 5:
        otre+=1
print(otre)

for i in range(len(lista)):
    if lista[i] % 10 == 7:
        hetre+=1
print(hetre)
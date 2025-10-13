import random
szam=random.randint(0, 20)
paros=0

for i in range(len(szam)):
    if(szam%2==0):
        paros+=1

print("paros szamok osszege:" paros)
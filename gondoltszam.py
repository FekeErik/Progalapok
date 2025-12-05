import random

bekeres=int(input("Adjon meg egy kétjegyű számot. "))
gondoltszam=random.randint(10,99)
probalkozasszam=0

if bekeres<9 or bekeres>98:
    print("Helytelen érték, próbálja újra")


while bekeres!=gondoltszam:
    if (bekeres>gondoltszam):
        print("A gondolt szám kisebb")
    elif(bekeres<gondoltszam):
        print("A gondolt szám nagyobb")
    bekeres = int(input("Próbálja újra: "))
    probalkozasszam+=1

if(bekeres==gondoltszam):
    print("Milyen profi")
    print("próbálkozások száma: ",probalkozasszam)

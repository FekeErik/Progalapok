paros=0
szam=int(input("Adjon meg egy számot, nulla a kilépéshez."))

while szam!=0:
    print(szam)
    print("adjon meg egy újabbat!")

if szam%2==0:
    paros+=1

print(f"{paros} darab páros szám van")
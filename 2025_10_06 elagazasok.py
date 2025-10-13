import math

# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

# kérjen be a felhasználótól egy számot, és mondja meg, hogy 10-el osztható-e? Ha nem, akkor írja ki az utolsó jegyét
# pl : 10 ki : tízzel osztható
# 12 ki: 10-el nem osztható, utolsó számjegy:2

if(szam % 10 == 0):
    print("Tízzel osztható")
else:
    print("tízzel nem osztható")
    print("az utolsó számjegy:" + str(szam % 10))

szam2=int(input("adja meg a másodikat:"))

if szam!=0:
    if szam2!=0:
        reciprok1=1/szam
        reciprok2=1/szam2
        print(reciprok1+reciprok2)
    else:
        print("A második számnak nincs reciproka")  
else:
    print("Az első számnak nincs reciproka")

#adja meg a két számnak gyökét

if(szam+szam2>=0):
    print(math.sqrt(szam+szam2))
else:
    print("A két szám összege negatív")

#logikai operátorok
#and, or, xor, not

if (szam != 0 and szam2 !=0):
    rec = 1/szam
    rec2 = 1/szam2
    print(rec+rec2)
else:
    print("A két számból valamelyik nulla")

# HF: bool algebra
#hf: 3 szam (lehet tört is), ezek egy haromszog oldala.
#1. Derékszögú-e?
#2. Egyenlőszárú-e?
#3. Szabályos-e?
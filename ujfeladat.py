import random

#lebegőpontos!!!! - float * törtek, röviden.

a=1.25
b=float(input("Adjon meg egy tizedes törtet:"))
print(b*4)

#generáljon ki [1,9] közötti tört számot kettő tizedesjegyre.

#c=(random.randint(100, 900)/100)
c = random.random() # [0, 1[
print(c)
#hf befelyezni

#szövegkezelés
szoveg = input("Adjon meg egy szöveget")
print(szoveg)
print("szöveg hossza:", len(szoveg))
print("első karakter", szoveg[0])
karakter=szoveg[0]
kod=ord(szoveg[0])
print(kod)

ujkod= kod + 1
ujkarakter= chr(ujkod)
print(ujkarakter)

a=random.randint(97,122)
b=random.randint(97,122)
c=random.randint(97,122)
print(a,b,c)

#kérje be a felhasználó keresztnevét! Generáljon neki egy jelszót, az első három karakteránek ascii kódját. 
#Ha nincs a név 3 jegyű, akkor kettő esetén a hossz érték legyen a szorzat 3. tagja. 1 esetén a szám köbe legyen
#pl Alma 65 * 108 * 109
#Co - 67 * 111 * 2
#G - 71* 71* 71

Keresztnév=input("Adjon meg egy keresztnevet")
if(len(Keresztnév>3)):
    if(len(Keresztnév)==2):
        
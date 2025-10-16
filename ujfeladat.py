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
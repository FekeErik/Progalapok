"""
Utasítás (szekvencia)
    -menj előre
    -fordulj
    -szívd be a levegőt
    -fújd ki a levegőt
    -...
    -írasd ki - print()
    -tárold el - változónév = érték
    -számold ki - változónév = <képlet>
    -kérd be - input("add meg: ")

Elágazás - (szelekció)
 - ha piros a lámpa akkor megállok
 - ha zöld, akkor megindulok.
 -ha fal van előttem, elfordulok
 -ha rudom, nem megy, gyakorlom
 ...
 -ha a bekért szám páros, akkor kiíratom, hogy páros.
 -különben kiíratom, hogy páratlan
 -ha a dobókocka értéke 5, akkor előre lépek 5-öt

 Ismétlés - ciklus - (iteráció)
 - Addig menj, amíg a tábla vam
 - Addig dobálj aprót a gépbe, amíg el nem éred az összeget
 - Üss bele 3 darab tojást
 - Addig tegyél bele cukrot, amíg édes
 -Addig gyakorolj, amíg meg nem érted
 -Addig fog a tanár piszkálni, amíg nem látja, hogy értem
"""

db = 12
print("Szám: ", db)
#szám utolsó számjegye páros-e?     
utolso_szamjegy = db % 10
print("Utolsó számjegy: ", utolso_szamjegy)
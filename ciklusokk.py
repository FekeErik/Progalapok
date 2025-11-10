import random as r
"""
Ciklusok - ismétlés - loop

#Számlálós - For ciklus
Végigmegy a megadott elemeken vagy intervallumon
for elem in 

Tesztelős - While
"""
for elem in range(1,11,1):
    print(elem,end="")
print()

for elem in range(0,21,2):
    print(elem, end=" ")

szoveg="Kalapács"
print(szoveg)
for karakter in szoveg:
    if((szoveg[karakter]))<len(szoveg):
        print(szoveg[karakter],end=",")
    else:
        print(karakter)

n=len(szoveg)

for index in range(0,n,1):
    print(str(index+1)+szoveg[index],end="")

#irasson ki 5 darab random indexet a szovegbol

# for db in range(0,5,1):
#     szam=r.randint(0,3)
#     print(szoveg[szam],end="")
# print()

for index in range(-1, -n-1, -1):
    ujszoveg+=szoveg[index]
    print(szoveg[index],end="")
print()
print(ujszoveg)

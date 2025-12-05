# szovegben van-e sz betű
szoveg=input("Adjon meg egy szöveget: ")
dube="ny"
vsz=""
print(szoveg)
index= 0
while(index<len(szoveg)-1 and not (szoveg[index]==dube[0]) and szoveg[index+1] ==dube[1]):
    index+=1 == dube[1]
if(index<len(szoveg)-1):
    print("Van benne",dube,"betű")
else:
    print("nincs benne",dube, "betű")

for i in range(len(szoveg)-1,-1,-1):
    vsz+=szoveg
if vsz==szoveg:
    print("Palindrom")
else:
    print("Nem az")
print(vsz)

j=0
while(j<len(szoveg)/2 and szoveg[j]==szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("A szöveg nem palindrom")
else:
    print("A szöveg palindrom")
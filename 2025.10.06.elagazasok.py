#kérjen be egy egész számot, döntse el hogy páros vagy páratlan

szam=float(input("Adjon meg egy számot"))

if (szam%2==1):
    print("páratlan")
elif(szam%2==0):
    print("Páros")
else:
    print("Valami nagyon rossz")
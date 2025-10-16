import random
import math

a=random.randint(8,76)*13
b=random.randint(8,76)*13
c=random.randint(8,76)*13

szamjegy = int(input("adjon meg egy számjegyet"))

print(a,b,c)

if(a % 10 == szamjegy or b % 10 ==szamjegy or c % 10 == szamjegy):
    print("Van közte "+str(szamjegy)+"re végződő")
else:
    print("nincs közötte "+str(szamjegy)+" re végződő.")
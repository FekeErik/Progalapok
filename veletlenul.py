import random

bekeres=int(input("Adja meg, hany szamot szeretne "))

for i in range(bekeres):
    szam=random.randint(-950,950)
    print(szam,end=" ")
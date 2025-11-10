import math
sec=int(input("Adjon meg egy számot"))
ora = sec // 3600
perc = (sec - ora * 3600) // 60
mp = sec % 60
print("óra", ora)
print("perc",perc)
print("másodperc", mp)

